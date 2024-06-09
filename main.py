import os
import sys

from Processors.CSVProcessor import CSVProcessor
from Processors.JSONProcessor import JSONProcessor

# Dodanie folderu Processors do ścieżki modułów Pythona
processors_path = os.path.join(os.path.dirname(__file__), 'Processors')
sys.path.append(processors_path)

# Pobieranie danych od użytkownika
column = int(input('Column: '))
row = int(input('Row: '))
object_index = int(input('ObjectID: '))

# Ścieżki do plików
csv_file_path = os.path.join('data', 'Rekrucsv.csv')
json_file_path = os.path.join('data', 'rekrujs.json')

# Uruchamianie klasy CSVProcessor
csv_processor = CSVProcessor(csv_file_path)
lines = csv_processor.count_lines()
value = csv_processor.get_value(column, row)
csv_absolute_path = csv_processor.get_absolute_path()
value_type = type(value).__name__

print(f'Number of lines in the CSV file: {lines}')
print(f'CSV file path: {csv_absolute_path}')
print(f'Value in column {column} row {row}: {value}')
print(f'Value type: {value_type}')
print('##############')

# Uruchamianie klasy JSONProcessoraaaaa
json_processor = JSONProcessor(json_file_path)
json_object_count = json_processor.count_objects()
json_absolute_path = json_processor.get_absolute_path()
json_result = json_processor.get_object(object_index)

print(f'Number of objects in json: {json_object_count}')
print(f'JSON file path: {json_absolute_path}')
print(f'Chosen object: {json_result}')
