import os
import json

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
