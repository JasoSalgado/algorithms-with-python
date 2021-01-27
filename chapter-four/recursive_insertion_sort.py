"""
Recursive insertion sort
"""

def recursive_insertion_sort(seq, i):
    if i == 0: return
    recursive_insertion_sort(seq, i-1)
    j = i

    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j], seq[j-1]
        j -= 1

recursive_insertion_sort(3, 3)




