import requests
import os, json
from tabulate import tabulate
from utils import log, apply_auth_creds
from utils import get_slug, process_action

def create_team():
    from constants import VERBOSE_COLOR_MAP
    from constants import VerbosityLevel

    data = get_slug()
    if data:
        sprint_slug = data['sprint_slug']
    else:
        return

    url = '{sprint_slug}' +  '/team/themes/'
    resp = process_action(url, sprint_slug)

    if resp.status_code == 200:
        r_json = resp.json()
        data = {
            'team_handle': '',
            'synopsis': '',
            'theme_choice': ','
        }
        j_data = json.dumps(data)
        
        
    else:
        r_json = resp.json()
        msg = '{color}' + r_json['emessage'] + '{default_color}'
        msg_ctx = {'color': VERBOSE_COLOR_MAP[VerbosityLevel.ERROR]}
        log(msg, msg_ctx)



def join_team():
    data = get_slug()
    if data:
        sprint_slug = data['sprint_slug']
    else:
        return

def handle_team_reg():
    while True:
        msg = """
        1. Create a team\n
        2. Join a team\n
        3. Exit\n
        """
        print msg
        inp = raw_input('Please press a number: ')
        if inp == '1':
            create_team()
            break
        elif inp == '2':
            join_team()
            break
        elif inp == '3':
            print 'bye'
            break
