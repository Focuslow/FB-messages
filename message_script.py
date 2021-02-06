import os
from extract import extract
import json
import unidecode
from name_checker import get_name
from collections import Counter
from location_get import location
from location_prompt import override_prompt

def message_script():
    main_path, dir = location()
    success = False
    override = True
    try:
        path = main_path+'\\my_json'
        os.mkdir(path)
        os.rmdir(path)
        pass
    except OSError:
        while not success:
            answer = override_prompt()
            if answer == "y":
                success = True
                override = True
            elif answer == "n":
                override = False
                break
            else:
                pass

    data = []
    exchanges = {}
    used_names = []

    for path in dir:
        new_path = main_path + '\\inbox\\' + path
        names = get_name(new_path)
        if names:
            used_names.extend(names)
            if len(used_names)>=10:
                name = max(Counter(used_names))
                name_fix = name.encode('latin1').decode('utf8')
                break
        elif names==[]:
            dir.remove(path)

    if not override:
        return main_path, name_fix

    print('Extracting data from folders .... please wait')
    if names:
        for path in dir:
            new_path = main_path + '\\inbox\\' + path
            person_data = extract(new_path,name_fix)
            if person_data == 0:
                continue
            else:
                data.append(person_data)
        try:
            path_test = main_path + "\\my_json\\"
            os.mkdir(path_test)
        except OSError:
            print("Directory already exists.")


        for i, v in enumerate(data):
            for name in list(v.keys()):
                name = name.replace(" ", "_")
                name = unidecode.unidecode(name)
                count = sum(list(list(data[i].values())[0].msg_count.values()))
                if count == 0:
                    continue
                else:
                    new_file = main_path + "\\my_json\\" + name + ".json"
                    with open(new_file, 'w') as json_file:
                        json.dump(list(data[i].values())[0].json_save(), json_file, indent=3)

    return main_path, name_fix