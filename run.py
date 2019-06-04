import json
import argparse
from pprint import pprint
from pathlib import Path

from slack import Users, Channels, Messages


def get_arguments():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--slack_log_path", help="Path of the folder where you extracted slack_log.zip")
    _args = _parser.parse_args()
    return _args


if __name__ == '__main__':
    args = get_arguments()

    output_path = Path("output")
    channels_path = output_path.joinpath("channels.csv")
    users_path = output_path.joinpath("users.csv")
    messages_path = output_path.joinpath("messages.csv")

    slack_log_path = Path(args.slack_log_path)
    channels = Channels(path=str(slack_log_path.joinpath("channels.json")))
    users = Users(path=str(slack_log_path.joinpath("users.json")))

    channels.parse().to_csv(str(channels_path))
    users.parse().to_csv(str(users_path))

    channel_and_ids = channels.get_channels()

    messages = Messages(path=str(slack_log_path))
    messages.p(channel_and_ids)
    messages.data_frame.to_csv(str(messages_path))
