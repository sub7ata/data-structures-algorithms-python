import random


def bubble_sort(lst):
    """BUBBLE SORT"""
    num = len(lst)
    for itm in range(0, num - 1):
        is_swapped = False
        
        for vlu in range(0, num - itm - 1):
            if lst[vlu] > lst[vlu + 1]:
                lst[vlu], lst[vlu + 1] = lst[vlu + 1], lst[vlu]
                is_swapped = True
        if not is_swapped:
            break
    return lst

def bubble_sort_asc(sequence):
    """BUBBLE SORT (ACCENDING ORDER)"""
    indexing_length = len(sequence)
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        
        for vlu in range(indexing_length - 1):
            if sequence[vlu] > sequence[vlu + 1]:
                sequence[vlu], sequence[vlu + 1] = sequence[vlu + 1], sequence[vlu]
                is_sorted = False
                
    return sequence

def bubble_sort_desc(arr):
    """BUBBLE SORT (DECENDING ORDER)"""
    n = len(arr)
    
    for i in range(n - 1, -1, -1):
        is_swapped = False
        
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        if not is_swapped:
            break
    return arr


if __name__ == "__main__":
    lst = [random.randint(10, 99) for _ in range(10)]
    print(f"\n\nBEFORE SORTING:\t\t\t{lst}")

    print(f"AFTER BUBBLE SORT:\t\t{bubble_sort(lst.copy())}")
    print(f"AFTER BUBBLE SORT(ASC):\t\t{bubble_sort_asc(lst.copy())}")
    print(f"AFTER BUBBLE SORT(DESC):\t{bubble_sort_desc(lst.copy())}")