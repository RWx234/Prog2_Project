import json
# import os.path
'''
def json_save(data, filename='drink_data.json'):
    if os.path.exists(filename) == "False":
        with open(filename, w)
            json_save(data, filename)
    else
        with open(drink_data.json, )
    with open(filename, 'a+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
'''


def json_save(data, filename):
    try:
        with open(filename) as file:
            file_data = json.load(file)
    except FileNotFoundError:
        file_data = {}
    file_data.append(data)
    with open(filename, "w") as file:
        json.dump(file_data, file)