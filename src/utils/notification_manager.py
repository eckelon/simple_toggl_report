from slackclient import SlackClient

from src.utils import conf_manager


def notify(channel, msg):
    sc = SlackClient(conf_manager.get_slack_token())


    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=msg,
    )

