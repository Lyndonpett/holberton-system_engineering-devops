#!/usr/bin/python3
'''Given employee ID, returns information about their todo list progress'''


import requests
import sys


def employeeTasks(employeeID):
    '''returns info about an employee'''

    # variables
    name = ''
    tasksList = []
    tasksCounter = 0

    # requests
    employeeReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todoReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(employeeID))

    # get json from requests
    name = employeeReq.json().get('name')
    todoJSON = todoReq.json()

    # increment through tasks
    for task in todoJSON:
        if task.get('completed') is True:
            tasksCounter += 1
            tasksList.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(name,
          tasksCounter, len(todoJSON)))

    for title in tasksList:
        print('\t {}'.format(title))

    return 0


if __name__ == '__main__':
    employeeTasks(sys.argv[1])
