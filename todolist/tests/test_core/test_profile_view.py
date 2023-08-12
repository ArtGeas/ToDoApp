import factory
import pytest
from django.contrib.auth import get_user
from rest_framework import status

from core.models import User


class LoginRequestFactory(factory.DictFactory):
    username = factory.Faker('user_name')
    password = factory.Faker('password')


@pytest.mark.django_db()
class TestProfileView:
    url = '/core/profile'

    def test_get_profile(self, auth_client):
        response = auth_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_unlogin_profile(self, client):
        response = client.get(self.url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
