from django.conf import settings


class TgClient:

    def __init__(self, token: str | None = None):
        self.__token = token if token else settings.BOT_TOKEN
