import json
from os import path, mkdir
import sys
from config import JSON_DIR


def load_data(name="dataset.json", dir_name=JSON_DIR):
    file_name = path.join(dir_name, name)
    if path.exists(file_name):
        with open(path.join(dir_name, name), "r") as file:
            data = json.load(file)
            return data
    else:
        print(f"Ошибка: нет такого файла {file_name}")
        sys.exit()


def save_data(data, name="dataset.json", dir_name=JSON_DIR):
    if not path.isdir(dir_name):
        mkdir(dir_name)
    with open(path.join(dir_name, name), "w") as file:
        json.dump(data, file)