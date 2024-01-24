import pathlib
from talon import Module, actions, resource
from typing import Callable, Tuple
from pathlib import Path
import csv
import json


# path = pathlib.Path("C:\\Users\\devcs\\AppData\\Local\\Microsoft\\PowerToys\\FancyZones\\applied-layouts.json")
path = "C:/Users/devcs/AppData/Local/Microsoft/PowerToys/FancyZones/applied-layouts.json"

# path =
# path = e

# with open(path) as f:
#     print(f.read())

@resource.watch(path)
def on_update(f):
    # use the updated file here
    print(type(f))
    data = f.read()

    json_patterns = json.loads(data)

    print(json_patterns)
