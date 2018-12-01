# Simple Toggl Report

## Why?

This is a very very simple script to automatically create a markdown file with my toggl activity for a day. This is useful for me in the stand-up daily meetings. It's written around the [matthewdowney/TogglPy](https://github.com/matthewdowney/TogglPy) library.

I'm using fish as my shell, but it's easy to adapt it to your bash/zsh shells. All custom settings are set in `load-variables-example.fish`, but you can load them in the way your shell needs.

## How?

**Using it as console utility:**

```
python3 -m venv toggle-tools-env
source toggle-tools-env/bin/activate.fish
pip install -r requirements.txt
source load-variables.fish
python -m src.generate_date_report -d YYYY-MM-DD
```

**Using it as web service:**

If you use it as a web service, It'll notify you in the slack channel of your preference (slack settings have to be set as env variables).
This way, you can deploy this on whatever service you want (I've prepared the Heroku procfile for you) and automate a post request every morning (i.e. crontab) so you can get your activity details directly on slack.


```
python3 -m venv toggle-tools-env
source toggle-tools-env/bin/activate.fish
pip install -r requirements.txt
source load-variables.fish
gunicorn --bind 0.0.0.0:5000 src.app:app
curl -X POST \
        'localhost:5000/report' \
        -H 'Content-Type: application/json' \
        -H 'cache-control: no-cache' \
        -d '{"token": "YOUR_TOGGLE_TOKEN","date":"2018-11-26"}'
```

## How does it look?

```
(toggle-tools-env)$ python -m src.generate_date_report -d 2018-11-26

Activity report for 2018-11-26
==============================

[Fancy project]
 * toggl super fancy task => 4h
 * another fancy task => 1h
[Not so fancy project]
 * task 1 => 2h
 * task 2 => 1h
 * task 3 => 0.5h


Total worked hours: 8.5h

---------------------------- Markdown Post ----------------------------
# Daily Standup 27-11-2018
## Yesterday:

### Fancy project
- toggl super fancy task
- another fancy task

### Not so fancy project
- task 1
- task 2
- task 3

## Today:
- 
-----------------------------------------------------------------------
