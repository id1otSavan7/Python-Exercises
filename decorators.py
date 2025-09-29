def firstDecor(func):
    def inner(*args, **kwargs):
        print("|" * 30)
        func(*args, **kwargs)
        print("|" * 30)
    return inner

def secondDecor(func):
    def inner(*args, **kwargs):
        print("\\" * 30)
        func(*args, **kwargs)
        print("/" * 30)
    return inner


@firstDecor
@secondDecor
def message(msg):
    print(msg)

message("Hello World!")