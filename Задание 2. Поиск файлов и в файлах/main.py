import re
import os

data_found = {}
time_pattern = r'\b\d{1,2}:\d{2}(:\d{2})?\b'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_pattern = r'\b(?:https?://|www\.)[^\s]+'
python_variable_pattern = r'[a-zA-Z]{1,}[a-zA-Z0-9_]{1,}'
date_pattern = r'\d{1,2}\.\d{1,2}\.\d{2,4}'
float_pattern = r'\b\d+\.\d+\b'
license_plate_pattern = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\b'

print('1. Время')
print('2. email-адреса')
print('3. url-адреса')
print('4. Корректные имена переменных в Питоне')
print('5. Даты в различных форматах')
print('6. Вещественные числа')
print('7. Номерные знаки российских транспортных средств')
user_input_types = input('Выберете, какие данные вам нужны: ')
user_input = input('Введите букву: ')
os.chdir('./Задание 2. Поиск файлов и в файлах/task2')
for x in os.listdir():
    file_pattern = re.compile(f'^{user_input}.*[0-9][a-zA-Z0-9]\.txt$', re.IGNORECASE)
    if file_pattern.match(x) and len(x.split('.')[0]) >= 7:
        with open(x, 'r', encoding='utf-8') as file:
            file_data = file.read()
            if '1' in user_input_types:
                times = re.findall(time_pattern, file_data)
            else:
                times = None
            if '2' in user_input_types:
                emails = re.findall(email_pattern, file_data)
            else:
                emails = None
            if '3' in user_input_types:
                urls = re.findall(url_pattern, file_data)
            else:
                urls = None
            if '4' in user_input_types:
                python_variables = re.findall(python_variable_pattern, file_data)
            else:
                python_variables = None
            if '5' in user_input_types:
                dates = re.findall(date_pattern, file_data)
            else:
                dates = None
            if '6' in user_input_types:
                floats = re.findall(float_pattern, file_data)
            else:
                floats = None
            if '7' in user_input_types:
                license_plates = re.findall(license_plate_pattern, file_data)
            else:
                license_plates = None
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
