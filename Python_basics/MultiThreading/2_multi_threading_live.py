import time
import threading

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
# cal_square(arr)
# cal_cube(arr)

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("total time the program took: ", (time.time() - t), "s")