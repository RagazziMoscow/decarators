from colors import red, green, yellow
import time
import json


def log_duration(func):
    def wrapped():
        start = time.time()
        func()
        end = time.time()
        duration = end - start

        if duration < 1:
            duration = str(round(duration * 1000, 2)) + ' мс'
        else:
            duration = str(round(duration, 2)) + ' c'
        duration = yellow(duration, style='bold')

        func_name = green(func.__name__, style='bold')
        print('Функция {0} -> {1}'.format(func_name, duration))
    return wrapped


def to_json(func):
    def wrapped():
        result = func()
        if type(result) == 'dict':
            result = json.dumps(result)
    return wrapped


@log_duration
def some_func():
    lst = [i for i in range(20)]
    for item in lst:
        print(item)


def _main():
    some_func()


if __name__ == '__main__':
    _main()
