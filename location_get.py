from location_prompt import location_prompt
import os

def location():
    success = False

    while not success:
        path = location_prompt()
        if path:
            try:
                main_path = path + '\\inbox'
                os.mkdir(main_path)
                os.rmdir(main_path)
                print("Directory found.")
                dir = os.listdir(path + '\\inbox')
                success = True

            except OSError:
                print("Directory not found.")
                success = False

        if not path:
            try:
                path = os.path.dirname(__file__)
                os.mkdir(path+'\\inbox')
                os.rmdir(path + '\\inbox')
                print("Not found")
                success = False

            except OSError:
                print("Path found")
                success = True
                path = os.path.dirname(__file__)

            dir = os.listdir(path+'\\inbox')

    return path, dir