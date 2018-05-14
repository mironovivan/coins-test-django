from distutils.util import strtobool


def str2bool(string):
    """
    Converts string to boolean.
    :param string: String to convert.
    """
    try:
        return bool(strtobool(string))
    except ValueError:
        return None
