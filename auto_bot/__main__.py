from utils.user import user_register, user_auth
from utils import config, constants
import json
import random
from utils.posts import create_post
from utils.like import like_posts_for_user

if __name__ == '__main__':
    no_of_users = random.randint(3, config.MAX_NO_OF_USERS)
    print("Number of users: ", no_of_users)
    for i in range(no_of_users):
        user = user_register()
        tokens = user_auth(user)
        no_of_posts_per_user = random.randint(3, config.MAX_POSTS_PER_USER)
        print("Number of posts per user {}: ".format(user['username']), no_of_posts_per_user)
        for j in range(no_of_posts_per_user):
            create_post(tokens['access'])

    with open(constants.PATH_TO_CREDS_FILE) as json_file:
        user_creds_obj = json.loads(json_file.read())
        json_file.close()

    for key in user_creds_obj:
        like_posts_for_user(key, user_creds_obj[key])
    print('Finished')