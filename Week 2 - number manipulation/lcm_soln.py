# Uses python3
# import sys

def gcd_pro(a, b):
    if b == 0:
        return a
    rem = a % b
    return gcd_pro(b,rem)

def lcm_naive(a, b):
    '''
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    '''
    return ( ( a * b ) / gcd_pro(a, b) )

if __name__ == '__main__':
    
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(int(lcm_naive(a, b)))

