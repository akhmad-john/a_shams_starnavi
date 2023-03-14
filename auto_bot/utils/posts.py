import json
from .core_funcs import post_request, fetch_random_wiki_post, write_created_post_ids_to_file
from . import constants

def create_post(access_token):
    headers = {
        "Authorization": "Bearer " + access_token
    }
    post = post_request(constants.PATH_POST_CREATE, fetch_random_wiki_post(), headers=headers)
    write_created_post_ids_to_file(json.loads(post.content)['id'])
