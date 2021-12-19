import time
import multiprocessing

def cal_square(n):
    print("Calculating square of the numbers")
    for i in n:
        time.sleep(5)
        print("Square: ", i * i)

def cal_cube(n):
    print("Calculating Cube of the numbers")
    for i in n:
        time.sleep(5)
        print("Cube: ", i * i * i)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")