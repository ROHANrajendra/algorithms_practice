# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    F=[]
    
    if (n <= 1):
        return n
    else:
        F=[0,1]
        for i in range(1,n):
            Fn = (F[len(F)-1] + F[len(F)-2]) % 10
            F.append(Fn)

    return Fn

if __name__ == '__main__':
    
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
