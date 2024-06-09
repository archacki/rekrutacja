import csv
import os
import json

column = int(input('Column: '))
row = int(input('Row: '))
object_index = int(input('ObjectID: '))

def count_csvlines(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        line_count = sum(1 for row in reader)
    return line_count

def get_value(file_path, column, row):
    with open(file_path) as file:
        reader = csv.reader(file)
        for current_row, data in enumerate(reader, start=1):
            if current_row == row:
                return data[column - 1]

def count_objects_in_json(json_path):
    with open(json_path) as file:
        data = json.load(file)
    return len(data) if isinstance(data, list) else 0

def get_object_json(json_path, object_index):
    with open(json_path) as file:
        data = json.load(file)
        if 0 < object_index <= len(data):
            return data[object_index - 1]
        else:
            return print('ERROR: Object number is outside the allowed range')

file_path = 'data/Rekrucsv.csv'
absolute_path = os.path.abspath(file_path)
lines = count_csvlines(file_path)
value = get_value(file_path, column, row)
value_type = type(value).__name__
print(f'Number of lines in the CSV file: {lines}')
print(f'CSV file path: {absolute_path}')
print(f'Value in column {column} row {row}: {value}')
print(f'Value type: {value_type}')
print('##############')
json_path = 'data/rekrujs.json'
json_object_count = count_objects_in_json(json_path)
json_absolute_path = os.path.abspath(json_path)
json_result = get_object_json(json_path, object_index)
print(f'Number of objects in json: {json_object_count}')
print(f'JSON file path: {json_absolute_path}')
print(f'Chosen object: {json_result}')