import json

import requests


def get_input_data(file_path, testcase_name):
    return get_data_from_json_file(file_path, testcase_name)


def get_data_from_json_file(file_path, data_key=None):
    with open(file_path) as f:
        try:
            json_obj = json.load(f)
            f.close()
            if data_key is None:
                return json_obj
            else:
                return json_obj.get(data_key)
        except FileNotFoundError:
            print(f"File {file_path} not found.  Aborting")


