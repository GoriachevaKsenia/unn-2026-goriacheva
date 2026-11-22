FROM python:3.13-alpine
WORKDIR /app
COPY bot/ bot/
CMD ["python", "-u", "-m", "bot"]
