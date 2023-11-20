import json
import os


def create_json_file(fixture_data, path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, path)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        json.dump(fixture_data, f)
        print("File created")


def split_currency_pair(currency_pair):
    return currency_pair[:3], currency_pair[3:]
