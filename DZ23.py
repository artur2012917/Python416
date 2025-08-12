#напишите программу , осуществляющую проверку, существует ли указанный файл. если файл существует, выведите на
#на экран имя этого файла и имя его директории, а также время последненого доступа к файлу. Если файл не существует,
#выведите соответствующее сообщение


import os

file_path = "test/test.txt"


if os.path.exists(file_path):
    directory, name = os.path.split(file_path)
    atime = os.path.getmtime(file_path)
    print(f"{name}({directory}) - время последнего доступа к файлу {atime} секунд")
else:
    print(f"Файл {file_path} не существует")
