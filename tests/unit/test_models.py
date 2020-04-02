"""
This file (test_models.py) contains the unit tests for the models.py file.
"""


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert new_user.email == 'dhiaeddine.elabidi@ensi-uma.tn'
    assert  new_user.hashed_password == 'Password123'
    assert not new_user.authenticated
    assert new_user.role == 'user'


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.hashed_password != 'MyNewPassword'
    assert new_user.is_correct_password('MyNewPassword')
    assert not new_user.is_correct_password('MyNewPassword2')
    assert not new_user.is_correct_password('Password1')


def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask User Management Example!" in response.data
    assert b"Need an account?" in response.data
    assert b"Existing user?" in response.data


def test_home_page_post(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Welcome to the Flask User Management Example!" not in response.data


def test_login_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data
