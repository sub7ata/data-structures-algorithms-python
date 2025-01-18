import random


def quick_sort(l,low,high):
    """QUICK SORT"""
    if high<=low:
        return 
    pivot = l[low]
    start = low
    end = high

    while low < high:

        while l[low] <= pivot and low < high:
            low = low + 1

        while l[high] > pivot and low <= high:
            high = high - 1

        if low < high:
            l[high],l[low] = l[low],l[high]

    l[high],l[start] = l[start],l[high]
    quick_sort(l,start,high-1)
    quick_sort(l,high+1,end)

    return l


def quick_sort_acs(arr):

    return quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):

    if first<last:

        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)

    return arr

def partition(arr,first,last):

    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


if __name__ == "__main__":
    arr = [random.randint(000, 999) for _ in range(10)]
    print(f"\nBEFORE SORTING:\t\t {arr}" )
    print(f"AFTER MERGE SORT:\t {quick_sort(arr,0,len(arr)-1)}")
    print(f"AFTER MERGE SORT:\t {quick_sort_acs(arr)}\n")