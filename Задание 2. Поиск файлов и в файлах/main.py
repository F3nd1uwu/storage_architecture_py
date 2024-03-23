import re
import fnmatch
import os

user_input = input('Введите букву: ')
os.chdir('task2')
for x in os.listdir():
    file_name = user_input + r'\w*\d{1}\w{1}.txt'
    if len(x) >= 7 and re.match(file_name, x):
        with open(x, 'r') as file:
            with open('result.txt', 'w') as res:
                res.write(re.findall(r'\d\d:\d\d:\d{0,2}', file))
