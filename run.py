import json
import argparse
from pathlib import Path


def get_arguments():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--json_path", help="slack_log_path(***.json)")
    _args = _parser.parse_args()
    return _args


if __name__ == '__main__':
    args = get_arguments()

    with open(Path(args.json_path), "r", encoding="utf-8") as f:
        log = json.load(f)
        print(log)
