from login import login
from register import register
from os.path import expanduser

class BColors():
    HEADER = '\033[97m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DARK = '\033[90m'
    HIGHLIGHT = '\033[100m'

API_DOMAIN_ROOT = 'http://192.168.1.154:8000/sprint-developer/v1/'

CONFIG_DIR = '.config'

HOME = expanduser("~")

CONFIG_PATH = HOME + '/' + CONFIG_DIR

HESPRINT_DIR = 'hesprint'

SPRINT_PATH = CONFIG_PATH + '/' + HESPRINT_DIR

CRED_FILE_NAME = 'credentials.json'

CRED_FILE_PATH = SPRINT_PATH + CRED_FILE_NAME

SLUG_FILE_NAME = 'slug.json'

SLUG_FILE_PATH = SPRINT_PATH + SLUG_FILE_NAME

COMMAND_MAP = {
        'login' : login,
        'register': register,
    }

class VerbosityLevel:
    ERROR = 100
    WARNING = 200
    INFO = 300
    SUCCESS = 400

VERBOSE_COLOR_MAP = {
    VerbosityLevel.ERROR: BColors.FAIL,
    VerbosityLevel.WARNING: BColors.WARNING,
    VerbosityLevel.INFO: BColors.DEFAULT,
    VerbosityLevel.SUCCESS: BColors.OKGREEN,
}
