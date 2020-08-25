# Uses python3
import sys
import numpy

def optimal_weight(W, w):
    # write your code here
    # weights = [[0 for x in range(len(w))] for x in range(W+1)]
    weights = numpy.zeros(shape=(len(w), W + 1), dtype=int)
    result = 0
    for i in range(len(w)):
        for j in range(1, W+1):
            if w[i] > j:
                weights[i, j] = weights[i-1, j]
            else:
                maxval = max(w[i] + weights[i-1, j - w[i]], 
                    weights[i - 1, j]
                )
                weights[i, j] = maxval
    result = weights[len(w) - 1, W]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
