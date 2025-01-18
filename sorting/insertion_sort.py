import random


def insertion_sort(lst):
    """INSERTION SORT"""
    for itm in range(1, len(lst)):
        key = lst[itm]
        j = itm - 1
        
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def insertion_sort_asc(lst):
    """INSERTION SORT (ACCENDING ORDER)"""
    n = len(lst)
    
    for i in range(1, n):
        temp = lst[i]
        key = i
        
        for j in range(i - 1, -1, -1):
            if lst[j] > temp:
                lst[j + 1] = lst[j]
                key = j
            else:
                break
        lst[key] = temp
                
    return lst

def insertion_sort_desc(arr):
    """INSERTION SORT (DECENDING ORDER)"""
    num = len(arr)
    
    for i in range(1, num):
        key = i
        temp = arr[i]
        
        while key > 0 and temp > arr[key - 1]:
            arr[key] = arr[key - 1]
            key -= 1
        arr[key] = temp
    return arr


if __name__ == "__main__":
    lst = [random.randint(10, 99) for _ in range(10)]
    print(f"\nBEFORE SORTING:\t\t{lst}")

    print(f"AFTER INSERTION SORT:\t{insertion_sort(lst.copy())}")
    print(f"AFTER INSERTION SORT:\t{insertion_sort_asc(lst.copy())}")
    print(f"AFTER INSERTION SORT:\t{insertion_sort_desc(lst.copy())}")