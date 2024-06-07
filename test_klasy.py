import csv
import os

class File_CSV:
    def __init__(self, file_path):
        self.file_path = file_path
        self.line_count = self.count_lines()
        self.absolute_path = os.path.abspath(file_path)

    def count_lines(self):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return sum(1 for row in reader)

    def get_value(self, column, row):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for current_row, data in enumerate(reader, start=1):
                if current_row == row:
                    try:
                        return data[column - 1]  # Kolumny w Pythonie są indeksowane od 0
                    except IndexError:
                        return None  # W przypadku, gdy kolumna nie istnieje

class CSVProcessor:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def display_info(self, column, row):
        lines = self.csv_file.line_count
        absolute_path = self.csv_file.absolute_path
        value = self.csv_file.get_value(column, row)

        print(f'Liczba linii w pliku: {lines}')
        print(f'Ścieżka do pliku: {absolute_path}')

        if value is not None:
            value_type = type(value).__name__
            print(f'Wartość w kolumnie {column} wierszu {row}: {value}')
            print(f'Typ danych wartości: {value_type}')
        else:
            print(f'Kolumna {column} lub wiersz {row} nie istnieje w pliku CSV.')

def main():
    file_path = input('Podaj ścieżkę do pliku CSV: ')
    column = int(input('Podaj numer kolumny: '))
    row = int(input('Podaj numer wiersza: '))

    csv_file = File_CSV(file_path)
    processor = CSVProcessor(csv_file)
    processor.display_info(column, row)

if __name__ == '__main__':
    main()