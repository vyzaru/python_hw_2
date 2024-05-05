def call_info_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами: {args} и именованными аргументами: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@call_info_decorator
def fibonacci_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_generator(10):
    print(num)