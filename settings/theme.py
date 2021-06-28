from os import path
import subprocess
import json

from .path import qtile_path

def load_theme():
    theme = "onedark" 

    config  = path.join(qtile_path, "config.json")
    if path.isfile(config):
        with open(config) as file:
            theme = json.load(file)["theme"]
    else:
        with open(config, "w") as file:
            file.write(f'{{"theme": "{theme}"}}\n')
    
    theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as file:
        return json.load(file)

if __name__ == "settings.theme":
    colors = load_theme()

