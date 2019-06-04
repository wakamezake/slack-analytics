# slack-analytics
Convert Slack messages exported in JSON format to CSV.

## Getting Started
### Prerequisites
Set up Python environment:
```shell
$ pipenv install
```

### Usage
#### Download slack_log.zip
See [Slack - Export your workspace data](https://get.slack.help/hc/en-us/articles/201658943-Export-your-workspace-data)

#### Extract slack_log.zip
```shell
$ unzip path\to\slack_log_zip
```

#### Run script
```shell
$ python run.py --slack_log_path path\to\extracted_slack_log_zip
```

#### Result
Directory structure
- output
	- messages.csv
	- users.csv
	- channels.csv
	
### CSV Format
#### messages.csv

|channel_id|ts|thread_ts|talk_user|text|
|:--|:--|:--|:--|:--|
|C5XXXXXXX|yyy-mm-dd hh:mm:ss.SSS|yyyy-mm-dd hh:mm:ss.SSS|U9XXXXXXX|`<@U8YYYYYYY>`hello|
|C5XXXXXXX|yyy-mm-dd hh:mm:ss.SSS|yyy-mm-dd hh:mm:ss.SSS|U8YYYYYYY|hoge|
|C5XXXXXXX|yyy-mm-dd hh:mm:ss.SSS|yyy-mm-dd hh:mm:ss.SSS|U9XXXXXXX|huga|