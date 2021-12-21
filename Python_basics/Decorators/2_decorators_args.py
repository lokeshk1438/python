# Link for below exercise
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PLYMhprV62E2axLz3pbp-xIhibN8_OWED8&index=6&t=249s

# decorator functionality
def decorator_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print("wrapper executed before {0}".format(orig_func.__name__))
        return orig_func(*args, **kwargs)
    return wrapper_func

@decorator_func # internally it gets assigned as display = decorator_func(display)
def display():
    print("This is a sample display")

# passing multiple arguments and surronding with decorator
@decorator_func
def display_info(name, age):
    print("display_info ran with arguments {0} {1}".format(name, age))

display_info("Test", 20)
