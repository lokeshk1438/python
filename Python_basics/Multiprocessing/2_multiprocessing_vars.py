import time
import multiprocessing

sq_res = []
def cal_square(n):
    print("Calculating square of the numbers")
    global sq_res
    for i in n:
        # time.sleep(5)
        print("Square: ", i * i)
        sq_res.append(i*i)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p1.start()
    p1.join()

    print("result is ", sq_res)
    print("Done")