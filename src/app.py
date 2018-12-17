from datetime import date

from flask import Flask, request, jsonify
from .Activity import Activity
from .utils import conf_manager, notification_manager, date_validator

app = Flask(__name__)


@app.route("/report", methods=['POST'])
def report():
    try:
        daily_date = date.today() if not 'date' in request.get_json() else date_validator.valid_date_type(
            request.get_json()['date'])
    except Exception:
        return jsonify({"status": 500, "msg": "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(
            request.get_json()['date'])})

    token = request.get_json()['token']
    slack_username = request.get_json()['slack_username']
    toggl_workspace_id = request.get_json()['toggl_workspace_id']

    if (token is None or token == ''
            or slack_username is None or slack_username == ''
            or toggl_workspace_id is None or toggl_workspace_id == ''):
        return jsonify({"status": 500, "msg": "Token, slack_username and toggl_workspace_id are required fields!"})

    markdown = Activity(token, daily_date, toggl_workspace_id).render()
    notification_manager.notify(slack_username, markdown)

    return jsonify(markdown)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
