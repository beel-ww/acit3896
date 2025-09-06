from typing import List
from math import floor

def linear_search(n: int, h: List[int]) -> int | None:
    for i, val in enumerate(h):
        if val == n:
            return i
    
    return None

# print(linear_search(8, [6, 2, 8, 4]))
# print(linear_search(4, [6, 2, 8, 4]))
# print(linear_search(5, [6, 2, 8, 4]))

def linear_search_multi(n: int, h: List[int]) -> List[int]:
    indexes: List[int] = []

    for i, val in enumerate(h):
        if val == n:
            indexes.append(i)

    return indexes

print(linear_search_multi(8, [6, 2, 8, 4, 8, 7]))
print(linear_search_multi(4, [6, 2, 8, 4, 8, 7]))
print(linear_search_multi(5, [6, 2, 8, 4, 8, 7]))

def binary_search(n: int, h: List[int]) -> int | None:
    start = 0
    end = len(h) - 1

    while start <= end:
        mid = floor((start+end)/2)

        if h[mid] == n:
            return mid
        elif h[mid] > n:
            end = mid - 1
        elif h[mid] < n:
            start = mid + 1
        
    return

# print(binary_search(8, [2, 4, 6, 8]))
# print(binary_search(2, [2, 4, 6, 8]))
# print(binary_search(1, [2, 4, 6, 8]))
# print(binary_search(99, [2, 4, 6, 8]))
# print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))
# print(binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))

def binary_search_multi(n: int, h: List[int]) -> List[int]:
    indexes: List[int] = []

    start = 0
    end = len(h) - 1

    while start <= end:
        mid = (start+end)//2

        if h[mid] == n:
            indexes.append(mid)
            
            left = mid - 1
            while left >= start and h[left] == n:
                indexes.append(left)
                left -= 1

            right = mid + 1
            while right <= end and h[right] == n:
                indexes.append(right)
                right += 1
            
            break

        elif h[mid] > n:
            end = mid - 1
        elif h[mid] < n:
            start = mid + 1

    return sorted(indexes)

print(binary_search_multi(3, [1, 2, 2, 3, 3, 3, 4, 5]))