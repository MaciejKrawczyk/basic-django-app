import json
import os


def create_json_file(fixture_data, path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, path)

    with open(file_path, 'w') as f:
        json.dump(fixture_data, f)
        print("File created")
