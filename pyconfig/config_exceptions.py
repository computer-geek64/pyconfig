#!/usr/bin/python3
# config_exceptions.py


class ConfigError(Exception):
    def __init__(self, message='Invalid configuration for environment variable conversion'):
        super(ConfigError, self).__init__(message)


class PythonConfigError(ConfigError):
    def __init__(self, message='Invalid Python configuration for environment variable conversion'):
        super(PythonConfigError, self).__init__(message)


class JSONConfigError(ConfigError):
    def __init__(self, message='Invalid JSON configuration for environment variable conversion'):
        super(JSONConfigError, self).__init__(message)


class EnvConfigError(ConfigError):
    def __init__(self, message='Invalid .env file configuration for environment variable conversion'):
        super(EnvConfigError, self).__init__(message)
