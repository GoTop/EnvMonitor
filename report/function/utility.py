# coding=utf-8

def merge(a, b, path=None):
    """
    "merges b into a"
    http://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge
    :param a:
    :param b:
    :param path:
    :return:
    """


    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a