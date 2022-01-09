from memory_profiler import memory_usage
import random
import time

names = ['john', 'adam', 'eve', 'sana']
majors = ['math', 'eng', 'cse', 'mpc']

c = zip(names, majors)

print("memory --> before --> {}MB".format(memory_usage()))
# print(list(c))

def people_list(num_people):
    res = []
    for i in range(int(num_people)):
        person = {
            "id" : i,
            "name" : random.choice(names),
            "major" : random.choice(majors)
        }
        res.append(person)
    return res

def people_generator(num_people):
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
        yield person

#
# t1 = time.time()
# peop = people_list(1000000)
# t2 = time.time()

t1 = time.time()
peop = people_generator(100000000)
t2 = time.time()

print("memory --> after --> {}MB".format(memory_usage()))
print("time taken in {0}s".format((t2-t1)))