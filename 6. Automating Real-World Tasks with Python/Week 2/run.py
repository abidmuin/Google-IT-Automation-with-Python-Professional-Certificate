#! /usr/bin/env python3

import os
import requests
import json

path = "/data/feedback"
files_dir = os.chdir(path)
feedback_files = os.listdir()
list.sort(feedback_files)

print(feedback_files)

dir = os.getcwd()
print(dir)
print()

for file in feedback_files:
    feedback_dict = {}
    dict_key = ['title', 'name', 'date', 'feedback']
    i = 0

    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        for i in range(len(dict_key)):
            feedback_dict[dict_key[i]] = lines[i].rstrip("\n")
        print(feedback_dict)

    except:
        print("Could not read the file")

    feedback_data = json.dumps(feedback_dict)
    #headers = {'Content-type': 'application/json'}
    #response = requests.post("http://35.192.131.255/feedback/", data=data,headers=headers)
    url = "http://104.197.11.178/feedback/"
    response = requests.post(url, json=feedback_dict)
    print("status_code " + str(response.status_code))
