# Simple Toggl Report

## Why?

This is a very very simple script to automatically create a markdown file with my toggl activity for a day. This is useful for me in the stand-up daily meetings. It's written around the [matthewdowney/TogglPy](https://github.com/matthewdowney/TogglPy) library

## How?

```
python3 -m venv toggle-tools-env
source toggle-tools-env/bin/activate
pip install -r requirements.txt
python src/generate_date_report.py -s YYYY-MM-DD
```

## How does it look?

```
(toggle-tools-env)$ python src/generate_date_report.py -d 2018-11-26

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
