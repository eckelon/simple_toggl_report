import configparser

config = configparser.ConfigParser()
config.read('conf.ini')


def get_token():
    return config['DEFAULT']['token']


def get_workspace_id():
    return config['DEFAULT']['workspace_id']


def get_default_project():
    return config['DEFAULT']['default_project']
