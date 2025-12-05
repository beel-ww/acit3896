
def pivot_naive(seq):
    # Honestly you can do almost anything here; heck, just return the last element of seq
    return seq[-1]

def partition_naive(seq, pivot):
    less = []
    equals = []
    greater = []

    for i in seq:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equals.append(i)
        else:
            greater.append(i)

    return [less, equals, greater]

def quicksort_naive(seq):
    if len(seq) <= 1:
        return seq
    
    pivot = pivot_naive(seq)

    left, pivs, right = partition_naive(seq, pivot)
    
    res = quicksort_naive(left) + pivs + quicksort_naive(right)
    seq[:] = res
    return quicksort_naive(left) + pivs + quicksort_naive(right)

def pivot_upgrade(seq, lo, hi):
    if lo >= hi or hi > len(seq) or lo < 0:
        raise ValueError("Bad indexes")
    
    return lo + (hi-lo) //2

def quicksort_upgrade(seq):
    __quicksort_upgrade(seq, 0, len(seq))

def __quicksort_upgrade(seq, lo, hi):
    if hi - lo <= 1:
        return
    
    pivot = pivot_upgrade(seq, lo, hi)
    lt, eq, gt = partition_upgrade(seq, pivot, lo, hi)
    __quicksort_upgrade(seq, lo, lo+lt)
    __quicksort_upgrade(seq, lo+lt+eq, hi)

# def partition_upgrade(seq, pivot, lo, hi):
#     [one, two, three] = partition_naive(seq[lo:hi], pivot)
#     seq[lo:hi] = one + two + three
#     return [len(one), len(two), len(three)]

def partition_upgrade(seq, pivot, lo, hi):
    # pivot_value = seq[pivot]
    # lo_ends = lo
    # pivot_i = lo + 1
    # hi_start = hi - 1

    # while pivot_i <= hi_start:
    #     if seq[pivot_i] < pivot_value:
    #         seq[lo_ends], seq[pivot_i], = seq[pivot_i], seq[lo_ends]
    #         lo_ends += 1
    #         pivot_i += 1
    #     elif seq[pivot_i] == pivot_value:
    #         pivot_i += 1
    #     else:
    #         hi_start -= 1
    #         seq[hi_start], seq[pivot_i] = seq[pivot_i], seq[hi_start]
    
    # lt, eq, gt = lo_ends - lo, hi_start - lo_ends, hi - hi_start

    # return lt, eq, gt

    seq[lo], seq[pivot] = seq[pivot], seq[lo]
    pivot = lo
    pivot_value = seq[pivot]

    lt = lo
    i  = lo + 1
    gt = hi

    while i < gt:
        if seq[i] < pivot_value:
            seq[lt], seq[i] = seq[i], seq[lt]
            lt += 1
            i += 1
        elif seq[i] == pivot_value:
            i += 1
        else:
            gt -= 1
            seq[i], seq[gt] = seq[gt], seq[i]

    return lt - lo, gt - lt, hi - gt

nums = [5,2,6,1,7,8,1]
quicksort_upgrade(nums)
print(nums)


