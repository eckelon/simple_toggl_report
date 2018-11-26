class Task(object):
    def __init__(self, name, project, hours=0.0):
        self._name = name
        self._project = project
        self._hours = hours

    @property
    def name(self):
        return self._name

    @property
    def project(self):
        return self._project

    @property
    def hours(self):
        return self._hours

    def __str__(self):
        return "{} ({}) -> {}h".format(self._name, self._project, self._hours)
