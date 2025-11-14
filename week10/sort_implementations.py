def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]

def selection_sort(seq):
    n = len(seq)

    for i in range(n):
        smallest = seq[i]
        swap = i

        for j in range(i+1, n):
            if seq[j] < smallest:
                smallest = seq[j]
                swap = j
        
        if i != swap:
            seq[i], seq[swap] = seq[swap], seq[i]

    return seq

print(selection_sort([5,3,6,8,1,9]))

def insertion_sort(seq):
    n = len(seq)

    for i in range(n):
        val = seq[i]
        zoo = i-1

        while zoo > -1 and seq[zoo] > val:
            seq[zoo+1] = seq[zoo]
            zoo -= 1
        
        seq[zoo+1] = val

    return seq

unnum = [i for i in range(11)]

unnum.reverse()

print(insertion_sort(unnum))