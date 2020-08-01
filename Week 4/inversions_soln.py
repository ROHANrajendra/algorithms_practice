# Uses python3
import sys
'''
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions
'''
count = 0
def merger(a, l, u, m):
    
    global count
    b = a[l:m+1]
    c = a[m+1:u+1]
    nb = len(b)
    nc = len(c)
    i, j, k = 0, 0, l

    while i < nb and j < nc:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
            
        else:
            a[k] = c[j]
            j += 1
            count +=1
        k += 1
    
    while i < nb:
        a[k] = b[i]
        i += 1
        k += 1
    while j < nc:
        a[k] = b[j]
        j += 1
        k += 1

# a=array l=lowerbound u=upperbound
def mergeSort(a, l, u):
    if l >= u:
        return a
    
    m = (l+u)//2
    mergeSort(a, l, m)
    mergeSort(a, m+1, u)
    merger(a, l, u, m)
    
    


'''
def merger(b,c):
    
    p = len(b)
    q = len(c)
    i,j = 0,0
    while i < p and j < q:
        if b[i]<c[j]:
            d.append(b[i])
            i+=1
        else:
            d.append(c[j])
            j+=1
            count += 1
    return d

def mergeSort(a):
    n = len(a)
    if n <= 1:
        return a
    m = n//2
    b = mergeSort(a[1:m])
    c = mergeSort(a[m+1:n])
    d = merger(b,c)
    return d

'''

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    count = 0
    n = len(a)
    #b, c, d = [],[],[]
    
    mergeSort(a, 0, n)
    print(count - n)

