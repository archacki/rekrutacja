import csv
import json
import os

column = int(input('Column: '))
row = int(input('Row: '))

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

file_path = 'Rekrucsv.csv'
absolute_path = os.path.abspath(file_path)
lines = count_csvlines(file_path)
value = get_value(file_path, column, row)
value_type = type(value).__name__
print(f'Number of lines in the CSV file: {lines}')
print(f'CSV file localization: {absolute_path}')
print(f'Value in column {column} row {row}: {value}')
print(f'Value type: {value_type}')

json_file_path = 'rekrujs.json'
json_object_count = count_objects_in_json(json_file_path)
print(f'Number of objects in json: {json_object_count}')