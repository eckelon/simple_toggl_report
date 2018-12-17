from datetime import timedelta

from toggl.TogglPy import Toggl
from .utils import toggl_urls, conf_manager

from .Task import Task


class Activity(object):
    def __init__(self, token, daily_date, workspace_id):
        self._daily_date = daily_date
        self._activity = {}
        self._total_hours = 0
        self._token = token
        self._workspace_id = workspace_id

    def millis_to_hours(self, millis):
        return round(millis / 3600000, 2)

    def _loadActiviy(self):
        toggl = Toggl()
        toggl.setAPIKey(self._token)
        self._report_date = self._daily_date - timedelta(1)
        self.friday_text = ''

        if self._report_date.isoweekday() is 6 or self._report_date.isoweekday() is 7:
            self._report_date = self._daily_date - timedelta(3 if self._daily_date.isoweekday() is 1 else 2)
            self.friday_text = " (Friday)"

        self.report_day = '{0:%Y-%m-%d}'.format(self._report_date)

        me_info = toggl.request(toggl_urls.me)
        self._username = me_info['data']['fullname']

        summary_url = toggl_urls.summary + "?workspace_id={}&since={}&until={}&user_agent=api_test".format(
            self._workspace_id, self.report_day, self.report_day)
        response = toggl.request(summary_url)

        activity = {}
        default_project = conf_manager.get_default_project()

        for data in response['data']:
            project_name = default_project if None == data['title']['project'] else data['title']['project']
            activity[project_name] = []
            for item in data['items']:
                hours = self.millis_to_hours(item['time'])
                self._total_hours += hours
                activity[project_name].append(Task(item['title']['time_entry'], project_name, hours).serialize())

        self._activity = activity
        return activity

    def render(self):
        self._loadActiviy()
        daily_day = '{0:%d-%m-%Y}'.format(self._daily_date)

        markdown_data = ["# {}'s Daily Standup {}".format(self._username, daily_day)]
        markdown_data.append("## Yesterday{}:".format(self.friday_text))

        print("\n\n{}'s Activity report for {}".format(self._username, self.report_day))
        print("==============================\n")

        for project, tasks in self._activity.items():
            markdown_data.append("\n### {}".format(project))
            print("[{}]".format(project))
            for task in tasks:
                markdown_data.append("- {}".format(task['name']))
                print(" * {} => {}h".format(task['name'], task['hours']))

        print("\nTotal worked hours: {}h\n".format(self._total_hours))

        markdown_data.append("\n## Today:")
        markdown_data.append("- ")

        markdown_text = "\n".join(markdown_data)

        print('---------------------------- Markdown Post ----------------------------')
        print(markdown_text)
        print('-----------------------------------------------------------------------')

        return markdown_text
