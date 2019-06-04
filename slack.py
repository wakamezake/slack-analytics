import json
import pandas as pd
from pandas.io.json import json_normalize
from pathlib import Path
from datetime import datetime


class Log:
    def __init__(self, path="data/users.json"):
        self.path = path
        self.data_frame = None

    def parse(self, separator="_"):
        with open(self.path, "r", encoding="utf-8") as f:
            log = json.load(f)
        df = json_normalize(log, sep=separator)
        self.data_frame = df


class Users(Log):
    def __init__(self, path="data/users.json"):
        super().__init__(path)

    def parse(self, separator="_"):
        with open(self.path, "r", encoding="utf-8") as f:
            log = json.load(f)

        df = json_normalize(log, sep=separator)
        df['display_name_custom'] = ""

        for index, row in df.iterrows():
            if row['profile_display_name_normalized'] == "":
                display_name_custom = row['name']
            else:
                display_name_custom = row['profile_display_name_normalized']
            df.at[index, 'display_name_custom'] = display_name_custom
        self.data_frame = df


class Channels(Log):
    def __init__(self, path="data/channnels.json"):
        super().__init__(path)

    def get_channels(self):
        return dict(zip(self.data_frame["name"], self.data_frame["id"]))


class Messages(Log):
    def __init__(self, path="data"):
        super().__init__(path)
        self.message_columns = ['channel_id', 'ts', 'thread_ts', 'talk_user', 'text']
        self.message_no_require_columns = ['subtype', 'thread_ts', 'reactions']
        self.reaction_columns = ['channel_id', 'talk_id', 'talk_user', 'reaction_user', 'emoji', 'date']
        self.mention_columns = ['channel_id', 'talk_id', 'talk_user', 'mention_user', 'date']

    def p(self, channel_and_ids):
        messages = []
        for message_path in Path(self.path).glob("*/*.json"):
            print(message_path)
            channel_name = message_path.parents[0].name
            df = pd.read_json(message_path, encoding='utf-8').fillna("")

            for col in self.message_no_require_columns:
                if col not in df.columns:
                    df[col] = ""

            df = df[df['subtype'] == ""]
            for index, row in df.iterrows():
                time_stamp = ""
                thread_time_stamp = ""
                if row['ts']:
                    time_stamp = self.time(row['ts'])

                if row['thread_ts']:
                    thread_time_stamp = self.time(row['thread_ts'])

                message = [channel_and_ids[channel_name],
                           time_stamp,
                           thread_time_stamp,
                           row['user'],
                           row['text']]
                messages.append(message)
        self.data_frame = pd.DataFrame(messages, columns=self.message_columns)

    # https://github.com/hfaran/slack-export-viewer/blob/master/slackviewer/message.py
    @staticmethod
    def time(ts):
        # Handle this: "ts": "1456427378.000002"
        ts_epoch = float(ts)
        return str(datetime.fromtimestamp(ts_epoch))
