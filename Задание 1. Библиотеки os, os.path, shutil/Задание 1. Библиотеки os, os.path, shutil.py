import os
import shutil

# 1. Распечатать текущую аудиторию
print('1.', os.getcwd())
user_input = input('Нажмите enter для продолжения')

# 2. Распечатать логин текущего пользователя операционной системы.
print('2. Ваш логин:', os.getlogin())
user_input = input('Нажмите enter для продолжения')

# 3. Распечатать тип операционной системы, расшифровать результат.
type_os = os.name
if type_os == 'nt':
    print('3. Ваша ОС: Windows')
elif type_os == 'mac':
    print('3. Ваша ОС: MacOS X')
elif type_os == 'posix':
    print('3. Ваша ОС: Linux или MacOS')
elif type_os == 'java':
    print('3. Вы запустили программу на виртуальной машине')
else:
    print('3. Нам не известна ваша ОС')
user_input = input('Нажмите enter для продолжения')

# 4. Проверить, существует ли файл 'test.txt'.
if os.path.exists('test.txt'):
    print(f"4. Файл '{'test.txt'}' существует.")
else:
    print(f"4. Файл '{'test.txt'}' не существует.")
user_input = input('Нажмите enter для продолжения')

# 5. Распечатать содержимое текущей папки.
print('5. Содержимое данной папки:', *os.listdir(), sep='\n')
user_input = input('Нажмите enter для продолжения')

# 6. Распечатать файловую структуру текущей директории с учётом вложенности.
print('6. Файловая структура текущей директории:')
for dirpath, dirnames, filenames in os.walk("."):
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
user_input = input('Нажмите enter для продолжения')

# 7. Создать папку 'test', предварительно проверив её отсутствие.
if os.path.exists('test'):
    print('7. Папка test уже существует')
else:
    os.mkdir('test')
    print('7. Папка успешно создана')
user_input = input('Нажмите enter для продолжения')

# 8. Перейти в созданную папку 'test' и убедиться, что она теперь является текущей.
os.chdir('test')
print('8. Мы перешли в директорию:', os.getcwd())
user_input = input('Нажмите enter для продолжения')

# 9. Запросить у пользователя имя файла и создать файл с таким именем в текущей папке, записав в него своё имя.
file_name = input('9. Введите имя файла: ')
user_name = input('Введите ваше имя: ')
text_file = open(file_name, 'w')
text_file.write(user_name)
text_file.close()
user_input = input('Нажмите enter для продолжения')

# 10. Проверить, успешно ли создан файл и является ли он файлом или папкой.
if os.path.exists(file_name):
    if os.path.isfile(file_name):
        print('10. ', file_name, 'является файлом.')
    else:
        print('10. ', file_name, 'является папкой.')
user_input = input('Нажмите enter для продолжения')

# 11. Распечатать абсолютный путь до созданного файла и его размер.
print('11. ', os.path.abspath(file_name), '\n', 'Файл занимает', os.path.getsize(file_name), 'байт.')
user_input = input('Нажмите enter для продолжения')

# 12. Скопировать файл на уровень выше под тем же именем.
shutil.copy(file_name, '../')
print('12. Файл скопирован успешно.')
user_input = input('Нажмите enter для продолжения')

# 13. Подняться на уровень выше и ещё раз распечатать содержимое папки с учётом вложенности.
os.chdir('../')
print('13. Файловая структура текущей директории:')
for dirpath, dirnames, filenames in os.walk("."):
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
user_input = input('Нажмите enter для продолжения')

# 14. Распечатать содержимое скопированного файла.
with open(file_name, 'r') as file:
    print('14.', file.readline())
user_input = input('Нажмите enter для продолжения')

# 15. Удалить папку 'test' со всем содержимым.
shutil.rmtree('test')
print('15. Папка успешно удалена.')
user_input = input('Нажмите enter для продолжения')

# 16. Удалить скопированный файл из текущей папки.
os.remove(file_name)
print('16. Файл успешно удален.')
user_input = input('Нажмите enter для продолжения')

# 17. Убедиться, что в текущей папке больше нет папки 'test' и созданного нами файла.
if not(os.path.exists('test')):
    print('17. Папки "test" не существует в данной директории')
else:
    print('17. Папка "test" существует в данной директории')

if not(os.path.exists(file_name)):
    print(f'17. Файла "{file_name}" не существует в данной директории')
else:
    print(f'17. Файл "{file_name}" существует в данной директории')
user_input = input('Нажмите enter для продолжения')
