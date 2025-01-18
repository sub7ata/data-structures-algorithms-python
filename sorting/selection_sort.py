import random


def selection_sort(lst):
    """SELECTION SORT"""
    for itm in range(len(lst) - 1):
        min_idx = itm

        for vlu in range(itm + 1, len(lst)):
            if lst[vlu] < lst[min_idx]:
                min_idx = vlu
        lst[itm], lst[min_idx] = lst[min_idx], lst[itm]
    return lst

def selection_sort_asc(arr):
    """SELECTION SORT (ACCENDING ORDER)"""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_desc(arr):
    """SELECTION SORT (DECENDING ORDER)"""
    num = len(arr)
    for i in range(num -1, 0, -1):
        max_idx = 0

        for j in range(1, i + 1):
            if arr[j] < arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


if __name__ == "__main__":
    lst = [random.randint(10, 99) for _ in range(10)]
    print(f"\n\nBEFORE SORTING:\t\t\t{lst.copy()}")

    print(f"AFTER SELECTION SORT:\t\t{selection_sort(lst.copy())}" )
    print(f"AFTER SELECTION SORT(ASC):\t{selection_sort_asc(lst.copy())}")
    print(f"AFTER SELECTION SORT(DESC):\t{selection_sort_desc(lst.copy())}" )