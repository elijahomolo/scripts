#!/usr/bin/env python

from pymongo import MongoClient
import pprint
import json

client = MongoClient()
db = client.wakari

projects = db.projects
users = db.users
option = raw_input("list, reset_status, reset_project:  ")

def list_project_status():
    for coll_document in projects.find():
        name = coll_document.get('name')
        status = coll_document.get('status')
        print( name + ' is ' +  status)

def update_project_status():
    status = raw_input("status: ")
    print("updating projects with status:" + ' ' + status)
    for coll_document in projects.find({'status': status}):
        print('Updating project {}'.format(coll_document.get('name')))
        projects.update({'_id': coll_document.get('_id')}, {'$set': {'status': 'running'}})
        print('Updated project {}'.format(coll_document.get('name')))

def reset_specific_project():
    project = raw_input("project: ")
    print("updating project: " + ' ' + project)
    for coll_document in projects.find({'name': project}):
        print('Updating project {}'.format(coll_document.get('name')))
        projects.update({'_id': coll_document.get('_id')}, {'$set': {'status': 'running'}})


if option == "list":
    list_project_status()
elif option == "reset_status":
    update_project_status()
elif option == "reset_project":
    reset_specific_project()
