import requests
import os
import json
from utils import log
import getpass

def login():
    from constants import API_DOMAIN_ROOT
    from constants import CONFIG_PATH
    from constants import SPRINT_PATH
    from constants import CRED_FILE_PATH
    from constants import BColors

    url = API_DOMAIN_ROOT + 'login/'
    email = raw_input('Email:')
    password = getpass.getpass()
    data = {
        'email': email,
        'password': password,
    }
    resp = requests.post(url, data=data)
    if not resp.status_code == 200:
        msg = '{color}Please check your credentials{default_color}'
        msg_ctx = {'color': BColors.FAIL}
        log(msg, msg_ctx)
        return

    credentials = resp.json()
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)

    if not os.path.exists(SPRINT_PATH):
        os.makedirs(SPRINT_PATH)
    with open(CRED_FILE_PATH, 'wb') as temp_file:
        json.dump(credentials, temp_file)
    msg = '{color}You have successfully logged in!{default_color}'
    msg_ctx = {'color': BColors.OKGREEN}
    log(msg, msg_ctx)
