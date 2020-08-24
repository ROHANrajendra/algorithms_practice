# Uses python3
import sys
import math

def get_change(m):
    #write your code here
    denom = [1, 3, 4]
    ways = [0] * (m +1)
    ways[0] = 0
    
    for i in range(1, m+1):
        # setting high value as default for comparision
        ways[i] = math.inf
        for coin in denom:
            if i >= coin: 
                temp = ways[i - coin] + 1
                if temp < ways[i]:
                    ways[i] = temp
            else:
                break
                
    return ways[m]

if __name__ == '__main__':
    
    m = int(sys.stdin.read())
    print(get_change(m))
