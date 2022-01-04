#!/usr/bin/python3
'''Gathering data from api and exporting to CSV'''

import json
import requests
from sys import argv


def saveTasksToJSON(employeeID):
    '''Gathering data from api and exporting to CSV'''

    # variables
    username = ''
    userDic = {}

    # requests
    employeeReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todoReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(employeeID))

    # get json from requests
    username = employeeReq.json().get('username')
    todoJSON = todoReq.json()

    userDic[employeeID] = []

    for task in todoJSON:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = username
        taskDict['completed'] = task.get('completed')

        userDic[employeeID].append(taskDict)

    with open('{}.json'.format(employeeID), 'w') as jsonFile:
        json.dump(userDic, jsonFile)


if __name__ == '__main__':
    saveTasksToJSON(argv[1])
