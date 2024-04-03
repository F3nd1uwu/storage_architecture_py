import re
import os

data_found = {}
time_pattern = r'\b\d{1,2}:\d{2}(:\d{2})?\b'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_pattern = r'\b(?:https?://|www\.)[^\s]+'
python_variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
date_pattern = r'\b\d{1,2}\.\d{1,2}\.\d{2,4}\b'
float_pattern = r'\b\d+\.\d+\b'
license_plate_pattern = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\b'

user_input = input('Введите букву: ')
os.chdir('C:/Code/storage_architecture_py/Задание 2. Поиск файлов и в файлах/task2')
for x in os.listdir():
    file_pattern = re.compile(f'^{user_input}.*[0-9][a-zA-Z0-9]\.txt$', re.IGNORECASE)
    if file_pattern.match(x) and len(x.split('.')[0]) >= 7:
        with open(x, 'r') as file:
            print(x)
            file_data = file.read()
            print(file_data)
            times = re.findall(time_pattern, file_data)
            emails = re.findall(email_pattern, file_data)
            urls = re.findall(url_pattern, file_data)
            python_variables = re.findall(python_variable_pattern, file_data)
            dates = re.findall(date_pattern, file_data)
            floats = re.findall(float_pattern, file_data)
            license_plates = re.findall(license_plate_pattern, file_data)
            data_found[x] = {
                'times': times,
                'emails': emails,
                'urls': urls,
                'python_variables': python_variables,
                'dates': dates,
                'floats': floats,
                'license_plates': license_plates}
            with open('../result.txt', 'w') as res:
                res.write(str(data_found))          
