#!/usr/bin/python3
# parse.py

import os
import json
from .config_exceptions import ConfigError, PythonConfigError, JSONConfigError, EnvConfigError


def parse_py(filename):
    with open(filename, 'r') as file:
        lines = [x for x in file.readlines() if x.strip()]

    for line in lines:
        if '=' in line.split('#', 1)[0]:
            k, v = map(lambda x: x.strip(), line.split('=', 1))
            os.environ[k] = str(eval(v))


def parse_json_obj(obj):
    if type(obj) != dict:
        raise JSONConfigError

    for k, v in obj:
        os.environ[str(k)] = str(v)


def parse_json(filename):
    try:
        with open(filename, 'r') as file:
            obj = json.loads(file.read())
    except json.decoder.JSONDecodeError:
        raise JSONConfigError from None

    parse_json_obj(obj)


def parse_env(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        try:
            k, v = map(lambda x: x.strip(), line.split('=', 1))
        except ValueError:
            raise EnvConfigError from None

        os.environ[k] = v[1:-1] if v.startswith('\"') and v.endswith('\"') or v.startswith('\'') and v.endswith('\'') else v
