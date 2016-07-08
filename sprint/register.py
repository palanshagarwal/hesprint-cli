import requests
import os, json
from utils import log, apply_auth_creds

def register(**kwargs):
    from constants import API_DOMAIN_ROOT
    from constants import VERBOSE_COLOR_MAP
    from constants import VerbosityLevel

    sprint_slug = kwargs['subcommand']

    if not sprint_slug:
        msg = '{color}Please enter a sprint slug to register{default_color}'
        msg_ctx = {'color': VERBOSE_COLOR_MAP[VerbosityLevel.ERROR]}
        log(msg, msg_ctx)
        return

    url = API_DOMAIN_ROOT + sprint_slug +  '/register/'
    data = {}
    data = apply_auth_creds(data)
    resp = requests.post(url, data=json.dumps(data))
    if resp.status_code == 200:
        r_json = resp.json()
        msg = '{color}' + r_json['message'] + '{default_color}'
        msg_ctx = {'color':
                VERBOSE_COLOR_MAP[r_json['verbosity_level']]}
        log(msg, msg_ctx)
    else:
        msg = '{color}' + r_json['emessage'] + '{default_color}'
        msg_ctx = {'color': VERBOSE_COLOR_MAP[VerbosityLevel.ERROR]}
        log(msg, msg_ctx)

