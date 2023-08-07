import pytest
from django.test import Client

@pytest.mark.django_db
class TestUserLoginAuthentication:
    """
    Test user signup
    """
    def test_user_signup(self):
        client = Client()
        response = client.post(
            '/core/signup',
            {'username': 'test_user', 'password': 'Qwe123!', 'password_repeat': 'Qwe123!'}
        )
        expected_response = {'id': 1, 'username': 'test_user', 'email': '', 'first_name': '', 'last_name': ''}
        assert response.status_code == 201
        assert response.data == expected_response
        

def test_user_login(self, authenticated_user: dict):
        """
        Test user login
        """
        client = authenticated_user.get('client')
        user = authenticated_user.get('user')
        password = authenticated_user.get('password')

        response = client.post(
            '/core/login',
            {'username': user.username, 'password': password},
            content_type='application/json',
        )
        expected_response = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        assert response.status_code == 200
        assert response.data == expected_response
