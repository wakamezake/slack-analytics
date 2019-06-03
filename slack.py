import json
import pandas as pd


class Log:
    def __init__(self, path="data/users.json"):
        self.path = path

    def parse(self, separator="_"):
        with open(self.path, "r", encoding="utf-8") as f:
            log = json.load(f)
        df = pd.io.json.json_normalize(log, sep=separator)
        return df


class Users(Log):
    def __init__(self, path="data/users.json"):
        super().__init__(path)

    def parse(self, separator="_"):
        with open(self.path, "r", encoding="utf-8") as f:
            log = json.load(f)

        df = pd.io.json.json_normalize(log, sep=separator)
        df['display_name_custom'] = ""

        for index, row in df.iterrows():
            if row['profile_display_name_normalized'] == "":
                display_name_custom = row['name']
            else:
                display_name_custom = row['profile_display_name_normalized']
            df.at[index, 'display_name_custom'] = display_name_custom
        return df


class Channels(Log):
    def __init__(self, path="data/channnels.json"):
        super().__init__(path)
