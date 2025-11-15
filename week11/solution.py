from typing import List

def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)

def merge_sort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    
    else:
        middle = n // 2
        left = merge_sort(seq[:middle])
        right = merge_sort(seq[middle:])
        vals = merge(left, right)
        for i in range(len(vals)):
            seq[i] = vals[i]
        return vals

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
print(merge_sort([33,1,66,7,5,33]))
