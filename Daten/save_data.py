import json
import datetime


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
        file_data = file_data.sort(key=lambda x: x['zeitpunkt'])
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
            line_data_min = {}
            line_data_max = {}
            for entry in file_data:
                line_data_av[entry["zeitpunkt"]] = entry["av_bak"]
                line_data_min[entry["zeitpunkt"]] = entry["min_bak"]
                line_data_max[entry["zeitpunkt"]] = entry["max_bak"]
            # inputs have to be sorted by datetime keys
            input_keys = list(line_data_av.keys())
            start = min(input_keys)
            end = max(input_keys)
            min_time = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M")
            max_time = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M")
            step = datetime.timedelta(minutes=1)
            key_range = []
            while min_time <= max_time:
                key_range.append(min_time)
                min_time += step
            bak_av_values = []
            bak_min_values = []
            bak_max_values = []
            for key in key_range:
                if key.strftime("%Y-%m-%d %H:%M") in input_keys:
                    if len(bak_av_values) == 0:
                        bak_av_values.append(line_data_av[key.strftime("%Y-%m-%d %H:%M")])
                        bak_min_values.append(line_data_min[key.strftime("%Y-%m-%d %H:%M")])
                        bak_max_values.append(line_data_max[key.strftime("%Y-%m-%d %H:%M")])
                    else:
                        bak_av_values.append(bak_av_values[-1] +
                                             line_data_av[key.strftime("%Y-%m-%d %H:%M")] - 0.0025)
                        bak_min_values.append(bak_min_values[-1] +
                                             line_data_min[key.strftime("%Y-%m-%d %H:%M")] - (0.2 / 60))
                        bak_max_values.append(bak_max_values[-1] +
                                             line_data_max[key.strftime("%Y-%m-%d %H:%M")] - (0.1 / 60))
                        # 0.025 = Average BAK-Reduction per Minute (0.1-0.2 pro Stunde)
                else:
                    bak_av_values.append(bak_av_values[-1] - 0.0025)
                    bak_min_values.append(bak_min_values[-1] - (0.2 / 60))
                    bak_max_values.append(bak_max_values[-1] - (0.1 / 60))
            line_data_av = {}
            line_data_min = {}
            line_data_max = {}
            for key in key_range:
                for value in bak_av_values:
                    line_data_av[key] = value
                    bak_av_values.remove(value)
                    break
                for value in bak_min_values:
                    line_data_min[key] = value
                    bak_min_values.remove(value)
                    break
                for value in bak_max_values:
                    line_data_max[key] = value
                    bak_max_values.remove(value)
                    break
            return line_data_av, line_data_min, line_data_max
        # calculate until 0.0 BAK
        last_bak = line_data_av[key_range[-1]]
        bak_null = round(last_bak / 0.0025, 0)
        # for minute in bak_null:

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
