#Uses python3

import sys

def comparator(a,b):

    temp = a
    a +=b
    b +=temp
    # print(a,b)
    i = 0
    while i < len(a) and i < len(b):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
        i += 1
    
    return 0


def largest_number(n):
    #write your code here
    # print(n)
    res = ""
    # print(comparator(n[0],n[1]))
    
    # sorting the list based on comparator func
    for i in range(len(n)):

        for j in range(0, len(n)-i-1):

            if comparator(n[j],n[j+1]) == -1:
                n[j], n[j+1] = n[j+1], n[j]

    for x in n:
        res += x
    return res

if __name__ == '__main__':
    # input = sys.stdin.read()
    data = sys.stdin.read().split()
    n = data[1:]
    print(largest_number(n))
    
