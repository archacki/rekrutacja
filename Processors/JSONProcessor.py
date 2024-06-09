import json
import os

class JSONProcessor:
    def __init__(self, json_path):
        self.json_path = json_path

    def count_objects(self):
        with open(self.json_path) as file:
            data = json.load(file)
        return len(data) if isinstance(data, list) else 0

    def get_object(self, object_index):
        with open(self.json_path) as file:
            data = json.load(file)
            if 0 < object_index <= len(data):
                return data[object_index - 1]
            else:
                return 'ERROR: Object number is outside the allowed range'

    def get_absolute_path(self):
        return os.path.abspath(self.json_path)