import json
import numpy as np
from operator import itemgetter

with open("source_file_2.json", "r") as file:
    projects = json.load(file)

projects = sorted(projects, key=itemgetter('priority'), reverse=False)


managers = []
watchers = []

for project in projects:
    for manager in project["managers"]:
        managers.append(manager)
    for watcher in project["watchers"]:
        watchers.append(watcher)


managers = np.unique(managers)
watchers = np.unique(watchers)

managers_output = {}
manager_projects = []
watchers_output = {}
watcher_projects = []

for manager in managers:
    for project in projects:
        if manager in project["managers"]:
            manager_projects.append(project["name"])
    managers_output[manager] = manager_projects
    manager_projects = []

for watcher in watchers:
    for project in projects:
        if watcher in project["watchers"]:
            watcher_projects.append(project["name"])
    watchers_output[watcher] = watcher_projects
    watcher_projects = []

# print(json.dumps(managers_output, indent=4))
# print(json.dumps(watchers_output, indent=4))

with open("managers.json", "w") as file:
    json.dump(managers_output, file, indent=3)

with open("watchers.json", "w") as file:
    json.dump(watchers_output, file, indent=3)
