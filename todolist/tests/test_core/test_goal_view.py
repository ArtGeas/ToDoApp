import factory
import pytest
from django.contrib.auth import get_user
from rest_framework import status

from core.models import User


@pytest.mark.django_db()
class TestGoalView:

    def test_goal_list(self, auth_client):
        url = '/goals/goal/list'
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_unlogin_goal_list(self, client):
        url = '/goals/goal/list'
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
