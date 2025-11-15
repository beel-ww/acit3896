from typing import List

def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)

def mergesort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    
    else:
        middle = n // 2
        left = mergesort(seq[:middle])
        right = mergesort(seq[middle:])
        return merge(left, right)

def merge(left: List[int], right: List[int]):
    i, j = 0, 0
    n = len(left)
    m = len(right)
    merged = []

    while i < n and j < m:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < n:
        merged.append(left[i])
        i += 1
    while j < m:
        merged.append(right[j])
        j += 1

    return merged

left = [1,3,6,8,9]
right = [2,4,5,7,10]

print(merge(left, right))
print(mergesort([33,1,66,7,5,33]))
