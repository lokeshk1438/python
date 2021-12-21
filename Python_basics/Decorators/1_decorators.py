# Link for below exercise
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PLYMhprV62E2axLz3pbp-xIhibN8_OWED8&index=6&t=249s

# def outer_func():
#     msg = "Hi"
#     def inner_func():
#         print(msg)
#
#     return inner_func
#
# func = outer_func()
# func()
# func()

# decorator functionality
def decorator_func(orig_func):
    def wrapper_func():
        print("wrapper executed before {0}".format(orig_func.__name__))
        return orig_func()
    return wrapper_func

# below code can be rewritten as
# def display():
#     print("This is a sample display")
# decorated_display = decorator_func(display)
# decorated_display()

@decorator_func # internally it gets assigned as display = decorator_func(display)
def display():
    print("This is a sample display")

display()