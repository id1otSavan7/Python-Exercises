def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        print(f"[LOG] Positional args: {args}")
        print(f"[LOG] Keyword args: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Returned: {result}")
        return result
    return wrapper

@log_call
def greet(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

greet("Lance")
greet("Lance", punctuation="?")