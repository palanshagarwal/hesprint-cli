import argparse

from constants import COMMAND_MAP

def process_args(options):
    command = options.command
    if command in COMMAND_MAP:
        COMMAND_MAP[command]()
    else:
        print 'Please enter an appropriate option'


def main():
    parser = argparse.ArgumentParser(
        description="Manage your submissions and team for hackathon")
    parser.add_argument('command', type=str)

    options = parser.parse_args()
    process_args(options)



