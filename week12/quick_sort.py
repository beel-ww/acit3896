def quick_sort(seq):
    return partition(seq, 0, len(seq) - 1)

def partition(seq, first, last):
    i = first
    j = last
    pivot = seq[(first + last) // 2]

    while i <= j:
        while seq[i] < pivot:
            i += 1
        while seq[j] > pivot:
            j -= 1
        
        if i <= j:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
            j -= 1
    
    if first < j:
        partition(seq, first, j)
    if i < last:
        partition(seq, i, last)

    return seq

nums = [24, 10, 17, 9, 5, 9, 1, 23, 300]

print(quick_sort(nums))