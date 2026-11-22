import unittest
from typing import Any

from fake import Fake

from bot.dispatcher import Dispatcher
from bot.handlers.message_text import MessageTextHandler
from bot.messenger import Messenger


class DispatcherRoutingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sent_messages: list[dict[str, Any]] = []

        def fake_send_message(**params):
            self.sent_messages.append(params)

        messenger: Messenger = Fake({"send_message": fake_send_message})
        self.dispatcher = Dispatcher(messenger)
        self.dispatcher.add_handlers(MessageTextHandler())

    def test_text_goes_to_text_handler(self) -> None:
        update = {"update_id": 1, "message": {"chat": {"id": 42}, "text": "Hello"}}

        self.dispatcher.dispatch(update)

        self.assertEqual(self.sent_messages, [{"chat_id": 42, "text": "Hello"}])

    def test_sticker_is_ignored(self) -> None:
        update = {
            "update_id": 1,
            "message": {"chat": {"id": 42}, "sticker": {"file_id": "sticker-file-id"}},
        }

        self.dispatcher.dispatch(update)

        self.assertEqual(self.sent_messages, [])

    def test_photo_is_ignored(self) -> None:
        update = {"update_id": 1, "message": {"chat": {"id": 42}, "photo": []}}

        self.dispatcher.dispatch(update)

        self.assertEqual(self.sent_messages, [])

    def test_update_without_message_is_ignored(self) -> None:
        self.dispatcher.dispatch({"update_id": 1})

        self.assertEqual(self.sent_messages, [])
