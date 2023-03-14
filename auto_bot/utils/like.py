import json
from .core_funcs import post_request
from . import constants, config
from .user import user_auth
import random

def like(access_token, post_id):
    headers = {
        "Authorization": "Bearer " + access_token
    }
    body = {"post_id": post_id}
    post = post_request(constants.PATH_POST_LIKE, body, headers=headers)
    return post.content


def like_posts_for_user(username, password):
    with open(constants.PATH_TO_POST_IDS_FILE) as json_file:
        post_ids_obj = json.loads(json_file.read())
        json_file.close()

    post_ids = post_ids_obj['post_ids']
    posts_to_like = random.sample(post_ids, random.randint(3, config.MAX_LIKES_PER_USER))
    tokens = user_auth({
        constants.USERNAME_FIELD: username,
        constants.PASSWORD_FIELD: password
    })
    for i in posts_to_like:
        like(tokens['access'], i)

