# Uses python3


def get_change(m):
    n=0
    while m:
        
        if m % 10 == 0:
            n = n + (m/10)
            break
        elif(m % 5 == 0):
            n = n + 1
            m = m - 5
        else:
            n += 1
            m -= 1
            
    return n

if __name__ == '__main__':
    m = int(input())
    print(int(get_change(m)))
