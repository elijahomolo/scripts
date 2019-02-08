from pymongo import MongoClient
import pprint
import json

client = MongoClient()

db = client.wakari

projects = db.projects
users = db.users
temp_project_list = []
output = {}

def get_projects():
    for coll_document in projects.find():
        temp_project_list.append(coll_document)

    for project in temp_project_list:
        output[project.get('name')] = {}
        output[project.get('name')]['users'] = project.get('team')

    for project, data in output.items():
        project_users = []
        if data.get('users'):
            for user in data.get('users', []):
                temp_user = users.find_one({'_id': user})
                project_users.append(
                {'username':temp_user.get('username'), 'active':temp_user.get('is_active')}
                )
        output[project]['users'] = project_users

get_projects()

print(json.dumps(output, indent=4))
