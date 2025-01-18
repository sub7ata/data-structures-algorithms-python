import random


def counting_sort_1(l=None,k=None):
    """COUNTING SORT"""
    output = [0] * len(l)
    count = [0] * k
    
    for i in l:
        count[i] = count[i]+1
        
    for i in range(1,k):
        count[i] = count[i] + count[i-1]
        
    for i in reversed(l):
        output[count[i]-1] = i
        count[i] = count[i] - 1
        
    for i in range(len(l)):
        l[i] = output[i]
        
    return l

def counting_sort_2(arr=None,max_val=None):
    """COUNTING SORT"""
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr


if __name__ == "__main__":
    arr = [random.randint(10, 99) for _ in range(10)]
    K = max(arr) + 1
    print(f"\nBEFORE SORTING:\t\t{arr}" )

    print(f"AFTER INSERTION SORT:\t{counting_sort_1(arr,K)}")
    print(f"AFTER INSERTION SORT:\t{counting_sort_2(arr,K)}")