# Uses python3
import sys

def get_majority_element_naive(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def majority_element(a):
    count = dict()
    for i in range(len(a)):
        if a[i] not in count:
            count[a[i]] = 1
        else: 
            freq = count.get(a[i])
            freq += 1
            count[a[i]] = freq
            if freq > len(a)/2:
                return a[i]
    return -1
            


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majority_element(a) != -1:
        print(1)
    else:
        print(0)
