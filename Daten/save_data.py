import json


def json_save(data, filename='drink_data.json'):
    with open(filename, 'a+') as file:
        file_data = json.load(file)
        file_data.append(new_data)

