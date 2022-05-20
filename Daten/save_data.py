import json


def json_save(data, filename):
    try:
        with open(filename, mode="r") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        file_data = []
    file_data.append(data)

    with open(filename, mode="w") as file:
        json.dump(file_data, file, indent=4)


def sort_data(filename):
    with open(filename, mode="r") as file:
        file_data = json.load(file)
        file_data = file_data.sort(key = lambda x:x['zeitpunkt'])
        print(file_data)
        return file_data
    with open(filename, mode="w") as file:
        json.dump(file_data, file, indent=4)
