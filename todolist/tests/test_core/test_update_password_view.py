import factory
import pytest
from django.urls import reverse
from rest_framework import status


class UpdatePasswordRequest(factory.DictFactory):
    old_password = factory.Faker('password')
    new_password = factory.Faker('password')


@pytest.mark.django_db()
class TestUpdatePasswordView:
    url = '/core/update_password'

    def test_auth_required(self, client):
        response = client.put(self.url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_failed_to_partial_update_passwords(self, auth_client):
        response = auth_client.patch(self.url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response.json() == {'detail': 'Method "PATCH" not allowed.'}

    def test_invalid_old_password(self, auth_client):
        data = UpdatePasswordRequest.build()

        response = auth_client.put(self.url, data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'old_password': ['Current password is incorrect']}

    def test_too_weak_new_password(self, client, user_factory, faker):
        data = UpdatePasswordRequest.build(new_password='test')
        user = user_factory.create(password=data['old_password'])
        client.force_login(user)

        response = client.put(self.url, data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            'new_password': [
                'This password is too short. It must contain at least 8 characters.',
                'This password is too common.',
            ]
        }

    def test_change_user_password(self, client, user_factory):
        data = UpdatePasswordRequest.build()
        user = user_factory.create(password=data['old_password'])
        client.force_login(user)

        response = client.put(self.url, data=data)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {}
        user.refresh_from_db()
        assert user.check_password(data['new_password'])
