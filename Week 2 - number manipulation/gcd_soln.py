# Uses python3
# import sys

def gcd_pro(a, b):
    
    ''' 
    Naive:
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
                
    return current_gcd
    '''
    if b == 0:
        return a
    rem = a % b
    return gcd_pro(b,rem)
    
    
    
    

if __name__ == "__main__":
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_pro(a, b))
