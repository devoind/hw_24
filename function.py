import os
import re

from constant_value import DATA_DIR
from werkzeug.exceptions import BadRequest


def do_processing(cmd: str, value: str, data: list[str]) -> list:
    if cmd == 'filter':
        result = list(filter(lambda rec: value in rec, data))
    elif cmd == 'map':
        col_num = int(value)
        result = list(map(lambda rec: rec.split()[col_num], data))
    elif cmd == 'unique':
        result = list(set(data))
    elif cmd == 'sort':
        reverse = value == 'desc'
        result = sorted(data, reverse=reverse)
    elif cmd == 'limit':
        result = data[:int(value)]
    elif cmd == "regex":
        res = re.compile(value)
        result = list(filter(lambda v: re.search(res, v), data))
    else:
        raise BadRequest
    return result


def do_query(params: dict) -> list:
    with open(os.path.join(DATA_DIR, params["file_name"])) as file:
        file_data = file.readlines()
    res = file_data
    if 'cmd1' in params.keys():
        res = do_processing(params['cmd1'], params['value1'], res)
    if 'cmd2' in params.keys():
        res = do_processing(params['cmd2'], params['value2'], res)
    if 'cmd3' in params.keys():
        res = do_processing(params['cmd3'], params['value3'], res)
    return res
