import random


def merge_sort(l,lindex,rindex):
    if rindex > lindex:
        mid = (lindex+rindex)//2
        merge_sort(l,lindex,mid)
        merge_sort(l,mid+1,rindex)
        merge(l,lindex,mid,rindex)
        return l

def merge(a,low,mid,high):
    l = a[low:mid+1]
    r = a[mid+1:high+1]
    i=j=0
    k=low
    while i<len(l) and j<len(r):
        if l[i] < r[j]:
            a[k] = l[i]
            k=k+1
            i=i+1
        else:
            a[k] = r[j]
            k=k+1
            j=j+1
    while i<len(l):
        a[k] = l[i]
        k=k+1
        i=i+1
    while j<len(r):
        a[k] = r[j]
        k=k+1
        j=j+1


if __name__ == "__main__":
    lst = [random.randint(10, 999) for _ in range(10)]
    print(f"\nBEFORE SORTING:\t\t {lst}" )
    print(f"AFTER MERGE SORT:\t {merge_sort(lst,0,len(lst)-1)}\n")