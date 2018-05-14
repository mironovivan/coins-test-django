import os

from utils.str2bool import str2bool


def getenv_string(setting, default=''):
    """
    Gets environment variable as string.
    :param setting: Name of environment variable.
    :param default: Default value in case if variable is not available.
    """
    return os.environ.get(setting, default)


def getenv_bool(setting, default=None):
    """
    Gets environment variable as boolean value.
    :param setting: Name of environment variable.
    :param default: Default value in case if variable is not available.
    """
    result = os.environ.get(setting, None)
    if result is None:
        return default
    return str2bool(result)
