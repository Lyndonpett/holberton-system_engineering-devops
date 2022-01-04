#!/usr/bin/python3
'''Gathering data from api and exporting to CSV'''

import csv
import requests
from sys import argv


def saveTasksToCSV(employeeID):
    '''Gathering data from api and exporting to CSV'''

    # variables
    username = ''
    allTasks = []

    # requests
    employeeReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todoReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employeeID))

    # get json from requests
    username = employeeReq.json().get('username')
    todoJSON = todoReq.json()

    for task in todoJSON:
        taskRow = []
        taskRow.append(employeeID)
        taskRow.append(username)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))
        allTasks.append(taskRow)

    with open('{}.csv'.format(employeeID), 'w') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(allTasks)

    return 0


if __name__ == '__main__':
    saveTasksToCSV(argv[1])
