import csv
import os

class CSVProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_lines(self):
        with open(self.file_path) as file:
            reader = csv.reader(file)
            line_count = sum(1 for row in reader)
        return line_count

    def get_value(self, column, row):
        with open(self.file_path) as file:
            reader = csv.reader(file)
            for current_row, data in enumerate(reader, start=1):
                if current_row == row:
                    return data[column - 1]

    def get_absolute_path(self):
        return os.path.abspath(self.file_path)