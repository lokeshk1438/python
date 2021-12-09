# First Class Functions
# YT : https://www.youtube.com/watch?v=kr0mpwqttM0

#### INTRO
# def square(x):
#     return x*x
#
# f = square(5)
# f1 = square
#
# print("square: " ,square)
# print("f: ", f)
# print("f1: ", f1)
# print("calling f1 function: ", f1(10))

# def my_cubes(x):
#     return x * x * x

# building an function which takes another function as an argument
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# lst = [1, 2, 3, 4, 5]
# squares = my_map(square, lst)
# squares_temp = list(map(lambda x: x*x, lst))
# cubes = my_map(my_cubes, lst)
#
# print("squares: ", squares)
# print("squares_temp: ", squares_temp)
# print("cubes: ", cubes)


# 2. ######################################
# returning function from another function

# def logger(msg):
#
#     def log_msg():
#         print("Log! ", msg)
#
#     return log_msg
#
# log = logger('Hi')
# log()

# 3. ######################################
# returning function from another function

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1("Heading1")
print_h1("Heading2")

print_h2 = html_tag('p1')
print_h2("paragraph1")
print_h2("paragraph2")
