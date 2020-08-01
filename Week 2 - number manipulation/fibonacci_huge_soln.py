# Uses python3


def pisperiod(modulo):
    prev = 1
    curr = 1
 
    period = 1
    while not (prev == 0 and curr == 1):
        temp = (prev + curr) % modulo
        prev = curr
        curr = temp
 
        period += 1
 
    return period
'''
def fib_mod(n,m):
    
    period = pisperiod(m)
    n = n % period
    prev, curr = 0,1
    if n<=1:
        return n
'''

def get_fibonacci_huge(n, m):
    
    period = pisperiod(m)
    n = n % period
    
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n,m))
