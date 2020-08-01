# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):
    loot = 0.
    nval = 0
    items = dict()
    i=0
    for i in range(n):
        items[(values[i]/weights[i])] = weights[i]
    items_arranged = sorted(items.items())
    items_arranged.sort(reverse = True)
    # print(items_arranged)
    i = 0
    
    while nval < capacity:
        
        if items_arranged[i][1] < (capacity - nval):
            loot += items_arranged[i][0] * items_arranged[i][1]
            nval += items_arranged[i][1]
        else:
            # loot += items_arranged[i][0] * (items_arranged[i][1]-(capacity-nval))
            # nval += (items_arranged[i][1]-(capacity-nval))
            loot += items_arranged[i][0] * ((capacity-nval))
            nval += ((capacity-nval))
        i += 1
        if i > (len(items_arranged))-1:
            break

    
    # print(nval)
    

    return loot


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.4f}".format(opt_value))
    # print(round(opt_value,4))

