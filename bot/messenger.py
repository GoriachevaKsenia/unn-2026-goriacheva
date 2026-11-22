from abc import ABC, abstractmethod
from typing import Any


class Messenger(ABC):
    """Интерфейс мессенджера: от него зависит вся логика бота (DIP)."""

    @abstractmethod
    def get_updates(self, **params: object) -> list[dict[str, Any]]:
        """Получить новые обновления."""

    @abstractmethod
    def send_message(self, **params: object) -> dict[str, Any]:
        """Отправить текстовое сообщение."""
