from decorators import log_duration, to_json, ignore_exceptions


@log_duration
def some_func():
    lst = [i for i in range(20)]
    for item in lst:
        # print(item)
        some_var = ((item + 10) * 1500) / 2
        print('Итерация')


@log_duration
def example():
    sum = 0
    for some_item in range(0, 15):
        sum += 2
    return sum


@to_json
def get_dict():
    return {"c": 0, "b": 0, "a": 0}


@ignore_exceptions(ZeroDivisionError)
def some_func_with_zero_div():
    number = 0
    return 50 / number


@ignore_exceptions(IndexError)
def some_func_with_index_err():
    lst = [1, 2, 3]
    return lst[3]


def _main():
    some_func()
    example()
    print(type(get_dict()))
    some_func_with_zero_div()
    some_func_with_index_err()

if __name__ == '__main__':
    _main()
