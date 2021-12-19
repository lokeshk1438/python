# https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=2

import time

def cal_square(n):
    print("Calculating square of the numbers")
    for i in n:
        time.sleep(0.2)
        print("Square: ", i * i)

def cal_cube(n):
    print("Calculating Cube of the numbers")
    for i in n:
        time.sleep(0.2)
        print("Cube: ", i * i * i)

arr = [2, 3, 4, 5]
t= time.time()
cal_square(arr)
cal_cube(arr)

print("total time the program took: ", (time.time() - t), "s")