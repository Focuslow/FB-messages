import os
import json

def get_name(path):
    dir = os.listdir(path)
    messages_test_list = []
    names =[]
    for i in range(1,len(dir)+1):
        messages_test_list.append('message_' + str(i) + '.json')

    for item in dir:
        if item in messages_test_list:
            msg_path = path + '\\' + item
            with open(msg_path) as json_file:
                data = json.load(json_file)

            if (len(data['participants'])) > 2 or (len(data['participants'])) == 1:
                return 0

            names = list(data['participants'][0].values())
            names.extend(list(data['participants'][1].values()))

    return names