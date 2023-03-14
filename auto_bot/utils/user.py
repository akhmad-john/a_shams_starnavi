import names
from . import constants
import random
import string
from .core_funcs import post_request, write_user_creds_to_file
from random_username.generate import generate_username
import json


def set_password():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str


def user_register():
    username, password = generate_username(1)[0], set_password()
    first_name, last_name = names.get_first_name(), names.get_last_name()
    body = {
        constants.USERNAME_FIELD: username,
        constants.FIRST_NAME_FIELD: first_name,
        constants.LAST_NAME_FIELD: last_name,
        constants.PASSWORD_FIELD: password
    }
    user = post_request(constants.PATH_USER_CREATE, body)

    if user.status_code != 201:
        raise ValueError("User cannot be created!")
    write_user_creds_to_file(username, password)
    return {
        constants.USERNAME_FIELD: username,
        constants.PASSWORD_FIELD: password
    }


def user_auth(user_data):
    tokens = post_request(constants.PATH_USER_AUTH, user_data)
    if tokens.status_code != 200:
        raise ValueError("Incorrect credentials")
    return json.loads(tokens.content)


