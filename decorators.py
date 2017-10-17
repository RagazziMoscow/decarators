from colors import color
import time
import json


def log_duration(func):
    def wrapper():
        func_name = func.__name__

        start = time.time()
        result = func()
        end = time.time()
        duration = end - start

        duration = round(duration * 10 ** 6, 2)
        duration = str(duration) + ' мкс'
        print('Функция {0} {2} {1}'.format(color(func_name, fg='green', style='bold'),
                                           color(duration, fg='red',
                                                 style='bold'),
                                           color('->', style='bold')))
        return result
    return wrapper


def to_json(func):
    def wrapped():
        result = func()
        if type(result) is dict:
            result = json.dumps(result)
        return result
    return wrapped


def ignore_exceptions(exception_class):
    def exception_decorator(func):
        def wrapper():
            try:
                func()
            except exception_class:
                print(color('Обнаружена ошибка', fg='red'))
                return None
        return wrapper

    return exception_decorator

if __name__ == '__main__':
    pass
