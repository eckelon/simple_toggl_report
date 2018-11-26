from toggl.TogglPy import Toggl
from Task import Task
from utils import toggl_urls, conf_manager
from datetime import timedelta

class Activity(object):
    def __init__(self, daily_date):
        self._daily_date = daily_date
        self._activity = {}
        self._total_hours = 0

    def millis_to_hours(self, millis):
        return round(millis / 3600000, 2)

    def _loadActiviy(self):
        toggl = Toggl()
        toggl.setAPIKey(conf_manager.get_token())
        self._report_date = self._daily_date - timedelta(1)
        report_day = '{0:%Y-%m-%d}'.format(self._report_date)

        url = toggl_urls.summary + "?workspace_id={}&since={}&until={}&user_agent=api_test".format(
            conf_manager.get_workspace_id(), report_day, report_day)
        response = toggl.request(url)

        activity = {}
        default_project = conf_manager.get_default_project()

        for data in response['data']:
            project_name = default_project if None == data['title']['project'] else data['title']['project']
            activity[project_name] = []
            for item in data['items']:
                hours = self.millis_to_hours(item['time'])
                self._total_hours += hours
                activity[project_name].append(Task(item['title']['time_entry'], project_name, hours))

        self._activity = activity

    def render(self):
        self._loadActiviy()
        report_day = '{0:%Y-%m-%d}'.format(self._report_date)
        daily_day = '{0:%d-%m-%Y}'.format(self._daily_date)
        friday_text = ""
        # saturday and sunday aren't work days!
        if self._report_date.isoweekday() is 6 or self._report_date.isoweekday() is 7:
            self._report_date = self._daily_date - timedelta(3 if self._daily_date.isoweekday() is 1 else 2)
            friday_text = " (Friday)"

        markdown_text = ["# Daily Standup {}".format(daily_day)]
        markdown_text.append("## Yesterday{}:".format(friday_text))
        print("\n\nActivity report for {}".format(report_day))
        print("==============================\n")

        for project, tasks in self._activity.items():
            markdown_text.append("\n### {}".format(project))
            print("[{}]".format(project))
            for task in tasks:
                markdown_text.append("- {}".format(task.name))
                print(" * {} => {}h".format(task.name, task.hours))

        print("\nTotal worked hours: {}h\n".format(self._total_hours))

        markdown_text.append("\n## Today:")
        markdown_text.append("- ")

        print('---------------------------- Markdown Post ----------------------------')
        print("\n".join(markdown_text))
        print('-----------------------------------------------------------------------')
