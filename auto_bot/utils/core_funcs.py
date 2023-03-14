import requests
from . import config, constants
import json


def post_request(path, body, headers=None):
    return requests.post(url=config.BASE_URL + path, json=body, headers=headers)


def fetch_random_wiki_post():
    wiki_post = requests.get(url='https://en.wikipedia.org/api/rest_v1/page/random/summary')
    response_content = json.loads(wiki_post.content)
    return {
        'title': response_content['title'],
        'content': response_content['extract']
    }


def write_user_creds_to_file(username, password):
    with open(constants.PATH_TO_CREDS_FILE) as json_file:
        user_creds_obj = json.loads(json_file.read())
        json_file.close()

    user_creds_obj[username] = password

    with open(constants.PATH_TO_CREDS_FILE, 'w') as json_file:
        json.dump(user_creds_obj, json_file, indent=4,  separators=(',',': '))
        json_file.close()


def write_created_post_ids_to_file(post_id):
    with open(constants.PATH_TO_POST_IDS_FILE) as json_file:
        post_ids_obj = json.loads(json_file.read())
        json_file.close()

    post_ids_obj['post_ids'].append(post_id)

    with open(constants.PATH_TO_POST_IDS_FILE, 'w') as json_file:
        json.dump(post_ids_obj, json_file, indent=4,  separators=(',',': '))
        json_file.close()
