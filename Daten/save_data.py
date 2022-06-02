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


def get_data(filename):
    try:
        with open(filename, mode="r") as file:
            file_data = json.load(file)
            return file_data
    except FileNotFoundError:
        file_data = "False"
        return file_data


def line_chart_data(filename):
    try:
        with open(filename, mode="r") as file:
            file_data = json.load(file)
            line_data_av = {}
            for entry in file_data:
                line_data_av[entry["zeitpunkt"]] = entry["av_bak"]
            # inputs have to be sorted by datetime keys
            return line_data_av
    except FileNotFoundError:
        file_data = "False"
        return file_data


def pie_chart_data(filename):
    try:
        with open(filename, mode="r") as file:
            file_data = json.load(file)
            pie_data = {}
            for entry in file_data:
                if entry["drink"] in pie_data.keys():
                    old_value = pie_data[entry["drink"]]
                    pie_data[entry["drink"]] = old_value + entry["vol"]
                else:
                    pie_data[entry["drink"]] = entry["vol"]
        pie_data_values = list(pie_data.values())
        pie_data_keys = list(pie_data.keys())
        return pie_data, pie_data_keys, pie_data_values
    except FileNotFoundError:
        pie_data_keys = "False"
        pie_data_values = "False"
        pie_data = "False"
        return pie_data, pie_data_keys, pie_data_values
