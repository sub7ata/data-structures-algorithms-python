import random


def shell_sort(arr):
    """SHELL SORT"""
    sublistcount = len(arr)//2

    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)

        sublistcount = sublistcount // 2
    return arr

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap

        arr[position]=currentvalue


if __name__ == "__main__":
    arr = [random.randint(000, 999) for _ in range(10)]
    print(f"\nBEFORE SORTING:\t\t {arr}" )
    print(f"AFTER SHELL SORT SORT:\t {shell_sort(arr)}\n")