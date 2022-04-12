def print_text1():
    print('Func 1.')
def print_text2():
    print('Func 2.')

def simple_decorator(fn):
    def wrapper():
        print('Run func.')
        fn()
        print('Stop func.')
    return wrapper

first_test_wrapper = simple_decorator(print_text1)
second_test_wrapper = simple_decorator(print_text2)

first_test_wrapper()
second_test_wrapper()

"""
@
"""
def simple_decorator(fn):
    def wrapper():
        print('Run func: ' + fn.__name__)
        fn()
        print('Stop func.')
    return wrapper

@simple_decorator
def print_text():
    print('Test func 1')

print_text()
