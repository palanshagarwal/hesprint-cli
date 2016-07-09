import os
import json, requests

def process_action(url, sprint_slug):
    from constants import API_DOMAIN_ROOT
    from constants import VERBOSE_COLOR_MAP
    from constants import VerbosityLevel

    if not sprint_slug:
        msg = '{color}Please enter a sprint slug {default_color}'
        msg_ctx = {'color': VERBOSE_COLOR_MAP[VerbosityLevel.ERROR]}
        log(msg, msg_ctx)
        return

    url = url.format(sprint_slug=sprint_slug)
    url = API_DOMAIN_ROOT + url
    data = {}
    data = apply_auth_creds(data)
    resp = requests.post(url, data=json.dumps(data))
    return resp

def log(msg, msg_ctx, line_break=True):
    from constants import BColors
    msg_ctx.update({'default_color':BColors.DEFAULT})
    if line_break:
        print msg.format(**msg_ctx)
    else:
        print msg.format(**msg_ctx),

def apply_auth_creds(ctx):
    from constants import CRED_FILE_PATH
    from constants import BColors
    
    if not os.path.exists(CRED_FILE_PATH):
        msg = "{color}Please login first{default_color}"
        msg_ctx = {'color': BColors.FAIL}
        log(msg, msg_ctx)
    else:
        with open(CRED_FILE_PATH, 'r') as fp:
            data = json.load(fp)
        ctx.update(data)
        return ctx

def save_slug(sprint_slug):
    from constants import SLUG_FILE_PATH
    from constants import SPRINT_PATH
    from constants import BColors

    if not os.path.exists(SPRINT_PATH):
        msg = "{color}Please login first{default_color}"
        msg_ctx = {'color': BColors.FAIL}
        log(msg, msg_ctx)
    else:
        data = {'sprint_slug': sprint_slug}
        with open(SLUG_FILE_PATH, 'wb') as fp:
            json.dump(data, fp)

def get_slug():
    from constants import SLUG_FILE_PATH
    from constants import SPRINT_PATH
    from constants import BColors

    if not os.path.exists(SLUG_FILE_PATH):
        msg = "{color}Please access the event first{default_color}"
        msg_ctx = {'color': BColors.FAIL}
        log(msg, msg_ctx)
        return
    else:
        with open(SLUG_FILE_PATH, 'r') as fp:
            data = json.load(fp)
        return data