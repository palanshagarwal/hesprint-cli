import argparse

from constants import COMMAND_MAP

def process_args(options):
    command = options.command
    kwargs = {'subcommand': options.subcommand}
    if command in COMMAND_MAP:
        COMMAND_MAP[command](**kwargs)
    else:
        print 'Please enter an appropriate option'


def main():
    parser = argparse.ArgumentParser(
        description="Manage your submissions and team for hackathon")
    parser.add_argument('command', type=str)

    parser.add_argument('subcommand', nargs='?', type=str)

    options = parser.parse_args()
    process_args(options)
