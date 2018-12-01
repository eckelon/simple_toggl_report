import os

def get_token():
    return os.environ['STR_TOGGL_TOKEN']


def get_workspace_id():
    return os.environ['STR_WORKSPACE_ID']


def get_default_project():
    return os.environ['STR_DEFAULT_PROJECT']


def get_slack_token():
    return os.environ['STR_SLACK_TOKEN']


def get_notification_channel():
    return os.environ['STR_NOTIFICATION_CHANNEL']
