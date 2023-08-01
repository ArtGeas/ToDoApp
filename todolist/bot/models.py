from django.db import models
from django.utils.crypto import get_random_string

from core.models import User


class TgUser(models.Model):
    chat_id = models.PositiveBigIntegerField(primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    verification_code = models.CharField(max_length=20, unique=True, null=True, blank=True)

    @property
    def is_verified(self) -> bool:
        return bool(self.user)

    @staticmethod
    def _generate_verification_code(self) -> str:
        return get_random_string(20)

    def update_verification_code(self) -> None:
        self.verification_code = self.update_verification_code()
        self.save(update_fields=['verification_code'])
