import json
import argparse
from pprint import pprint
from pathlib import Path

from slack import Users, Channels


def get_arguments():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--json_path", help="slack_log_path(***.json)")
    _args = _parser.parse_args()
    return _args


if __name__ == '__main__':
    args = get_arguments()

    # channnels = Channels(path=args.json_path)
    users = Users(path=args.json_path)
    # pprint(channnels.parse())
    pprint(users.parse())
