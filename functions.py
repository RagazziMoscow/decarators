from decorators import log_duration, to_json


@log_duration
def some_func():
    lst = [i for i in range(20)]
    for item in lst:
        # print(item)
        some_var = ((item + 10) * 1500) / 2
        print('Итерация')


@log_duration
def example():
    return 'cekavo'


@to_json
def get_dict():
    return {"c": 0, "b": 0, "a": 0}


def _main():
    some_func()
    example()
    print(type(get_dict()))

if __name__ == '__main__':
    _main()
