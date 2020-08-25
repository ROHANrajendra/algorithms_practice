# Uses python3
import sys
import math

class primitiveCalculator:

    def __init__(self):
        pass

    def add1(self, x):
        return (int)(x-1)
    def x2(self, x):
        return (int)(x/2)
    def x3(self, x):
        return (int)(x/3)
    


def optimal_sequence(n):
    sequence = []
    cal = primitiveCalculator()
    min_seq = [None] * (n + 1)
    min_seq[0], min_seq[1] = 0, 0
    sequence.append([0])
    sequence.append([1])
    
    for i in range(2, n+1):
        min_seq[i] = math.inf
        temp2 = math.inf
        temp3 = math.inf

        if i % 3 == 0:
            temp3 = min_seq[cal.x3(i)] + 1
        if i % 2 == 0:
            temp2 = min_seq[cal.x2(i)] + 1
        temp1 = min_seq[i-1] + 1
        minval = min(temp1, temp2, temp3)
        min_seq[i] = minval

        if minval == temp1:
            sequence.append(sequence[cal.add1(i)] + [i])
            continue
        if minval == temp2:
            sequence.append(sequence[cal.x2(i)] + [i])
            continue
        if minval == temp3:
            sequence.append(sequence[cal.x3(i)] + [i])
    
    return sequence[-1]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')



