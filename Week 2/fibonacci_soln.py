# Uses python3
def calc_fib(n):
    F=[]
    
    if (n <= 1):
        return n
    else:
        F=[0,1]
        for i in range(1,n):
            Fn = F[len(F)-1] + F[len(F)-2]
            F.append(Fn)
            
    return Fn



n = int(input())
print(calc_fib(n))
