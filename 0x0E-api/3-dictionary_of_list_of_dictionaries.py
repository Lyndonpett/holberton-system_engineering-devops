#!/usr/bin/python3
'''saves all of the dictionaries'''

import json
import requests
from sys import argv

from requests.api import request


def saveALLtoJSON():
    '''saves all dicts to json'''

    # variables
    usersAndTasks = {}

    # do the requests and transport to json
    usersJSON = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()
    todoJSON = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    userInfo = {}

    for user in usersJSON:
        userInfo[user['id']] = user['username']

    for task in todoJSON:
        if usersAndTasks.get(task['userId'], False) is False:
            usersAndTasks[task['userId']] = []

        taskDict = {}
        taskDict['username'] = userInfo[task['userId']]
        taskDict['task'] = task['title']
        taskDict['completed'] = task['completed']

        usersAndTasks[task['userId']].append(taskDict)

    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(usersAndTasks, jsonFile)


if __name__ == '__main__':
    saveALLtoJSON()
