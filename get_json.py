import json
import os

from words_used import words_used
from grapher import graph
from plotter import plotppl

def get_json(path_start):
    main_path = path_start + '\\my_json'
    dir = os.listdir(main_path)
    data = {}
    # timedown = 0
    # timeup = 0

    for item in dir:
        path = main_path + '\\' + item
        with open(path, 'r') as json_file:
            stuff = json_file.read()
            info = json.loads(stuff)
            name = item[0:-5]
            data.update({name: info})

    return data

# #plotppl(data)
# words_me, words_you = words_used(data["Patricia_Robotova"],timedown, timeup)
# graph(words_me, words_you)

