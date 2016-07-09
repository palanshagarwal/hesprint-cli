import requests
import os, json
from tabulate import tabulate
from utils import log, apply_auth_creds
from utils import get_slug, process_action

def create_team():
    from constants import VERBOSE_COLOR_MAP
    from constants import VerbosityLevel
    from constants import FILE_DELIMETER
    from constants import TEAM_FILE_PATH

    data = get_slug()
    if data:
        sprint_slug = data['sprint_slug']
    else:
        return

    url = '{sprint_slug}' +  '/themes/'
    resp = process_action(url, sprint_slug)

    if resp.status_code == 200:
        r_json = resp.json()
        data = {
            'team_handle': '',
            'synopsis': '',
            'theme_choice': '',
        }
        j_data = json.dumps(data, indent=6)
        j_data += '\n'
        j_data += FILE_DELIMETER
        j_data += '\nPlease chose a theme from below:\n'

        master = []
        count = 1
        for k in r_json:
            master.append(str(count)+'. '+r_json[str(count)])
            count += 1
        theme_choice_data = '\n'.join(k for k in master)
        j_data += theme_choice_data + '\n'

        with open(TEAM_FILE_PATH, 'wb') as fp:
            fp.write(j_data)

        os.system('vi '+TEAM_FILE_PATH)
        with open(TEAM_FILE_PATH, 'r') as fp:
            data = fp.read()

        post_data = json.loads(data.split(FILE_DELIMETER)[0].strip())

        
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
