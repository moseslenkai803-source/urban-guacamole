def log_deco(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
@log_deco
def hello(name, greeting="Hello"):
    return f"{greeting}, {name}!"

@log_deco
def add(a, b):
    return a + b

print(add(a=5, b=10))
print(hello(name="Alice", greeting="Hi"))