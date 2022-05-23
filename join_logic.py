from exceptions import *


def join(file_name,file_names):
    if file_name == '':
        raise NameErrorCustom()
    if len(file_names) < 2:
        raise LengthError()

    for file in file_names:
        with open(file, 'r') as f:
            text = f.read()
        with open(file_name, 'a') as fi:
            fi.write(text)