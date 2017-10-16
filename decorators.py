from colors import color
import time
import json


def log_duration(func):
    def wrapped(*args, **kwargs):
        func_name = func.__name__

        start = time.time()
        result = func()
        end = time.time()
        duration = end - start

        duration = round(duration * 1000, 2)
        duration = str(duration) + ' мс'
        print('Функция {0} {2} {1}'.format(color(func_name, fg='green', style='bold'),
                                           color(duration, fg='red', style='bold'),
                                           color('->', style='bold')))
        return result
    return wrapped


def to_json(func):
    def wrapped():
        result = func()
        if type(result) is dict:
            result = json.dumps(result)
        return result
    return wrapped


if __name__ == '__main__':
    pass
