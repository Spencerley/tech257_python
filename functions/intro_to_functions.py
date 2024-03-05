# Why use functions?
# Principle: DRY (Don't Repeat Yourself)

def print_something(print_string):
    print(print_string)


def addition(int1=10, int2=200) -> int:
    return int1 + int2

# * next to it means any number of args can be passed in


def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


def greeting(name: str):
    print('hello my name is ' + name)


str_to_print = 'hello'
print_something(str_to_print)
print(addition(60, 9))
multi_args(1, 12, 30, 85)
greeting(84373)
