import os
from get_data import get_data
from Person import Person
from Exchange import Exchange


def extract(person_path,name):
    dir = os.listdir(person_path)
    messages_test_list = []
    data = {}
    for i in range(1,len(dir)+1):
        messages_test_list.append('message_' + str(i) + '.json')

    for item in dir:
        if item in messages_test_list:
            msg_path = person_path + '\\' + item
            if data:
                add_data = get_data(msg_path)
                for key in add_data.keys():
                    if key != 'names':
                        data[key].update(add_data[key])
            else:
                data = get_data(msg_path)
                if data == 0:
                    return 0

    names = data['names']
    try:
        names.remove(name)
    except ValueError:
        return 0
    out_data = Exchange(data[name], data[names[0]])
    return {names[0]: out_data}
    # out_data.printer()
    # out_data.me.printer()
    # out_data.you.printer()
