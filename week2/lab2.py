import time
import statistics
import random
from typing import List

means: List[int] = []
deltas = []
num_tests = 1000

def add_front(num):
    one_num = [1]
    nums_list = [i for i in range(num)]
    
    for _ in range(num_tests):
        start_time = time.perf_counter()
        new_list = one_num + nums_list
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def apnd(num):
    nums_list = [i for i in range(num)]
    
    for _ in range(num_tests):
        start_time = time.perf_counter()
        new_list = nums_list.append(1)
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def remove_front(num):
    nums_list = [i for i in range(num)]
    
    for _ in range(num_tests):
        start_time = time.perf_counter()
        new_list = nums_list[1:]
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def popping(num):
    for _ in range(num_tests):
        nums_list = [i for i in range(num)]
        start_time = time.perf_counter()
        new_list = nums_list.pop()
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def linear_search(n, h):
    if h in n:
        return True
    return False

def linear_exists(num):
    def list_with_guaranteed_number(num, guaranteed):
        num_list = [random.randint(0, 1) for _ in range(num)]
        index = random.randint(0, num-1)
        num_list[index] = guaranteed
        return num_list

    for _ in range(num_tests):
        haystack = list_with_guaranteed_number(num, 5)

        start_time = time.perf_counter()
        linear_search(haystack, 5)
        end_time = time.perf_counter()
        
        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def linear_existnt(num):
    nums = [0 for _ in range(num)]

    for _ in range(num_tests):
        start_time = time.perf_counter()
        linear_search(nums, 1)
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def key_check(dct, key):
    if key in dct:
        return True
    return False

def dct_exists(num):
    d = {}
    for i in range(num):
        d[i] = 0
    
    for _ in range(num_tests):
        start_time = time.perf_counter()
        key_check(d, 1)
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

def dct_existnt(num):
    d = {}
    for i in range(num):
        d[i] = 0

    for _ in range(num_tests):
        start_time = time.perf_counter()
        key_check(d, num+1)
        end_time = time.perf_counter()

        delta = (end_time - start_time) * 1000
        deltas.append(delta)
    means.append(statistics.mean(deltas))
    deltas.clear()

add_front(10)
add_front(1000000)

apnd(10)
apnd(1000000)

remove_front(10)
remove_front(1000000)

popping(10)
popping(1000000)

linear_exists(10)
linear_exists(1000000)

linear_existnt(10)
linear_existnt(1000000)

dct_exists(10)
dct_exists(1000000)

dct_existnt(10)
dct_existnt(1000000)

with open("./means.txt", "w") as f:
    for mean in means:
        f.write(str(mean) + "\n")