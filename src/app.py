from datetime import date

from flask import Flask, request, jsonify
from .Activity import Activity
from .utils import conf_manager, notification_manager, date_validator

app = Flask(__name__)


@app.route("/report", methods=['POST'])
def report():
    try:
        daily_date = date.today() if not 'date' in request.get_json() else date_validator.valid_date_type(request.get_json()['date'])
    except Exception:
        return jsonify({"status": 500, "msg": "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(
            request.get_json()['date'])})

    token = request.get_json()['token']

    if (token is None or token == ''):
        return jsonify({"status": 500, "msg": "Wrong token or user"})

    markdown = Activity(token, daily_date).render()
    notification_manager.notify(conf_manager.get_notification_channel(), markdown)

    return jsonify(markdown)

if __name__ == "__main__":
    app.run(host='0.0.0.0')