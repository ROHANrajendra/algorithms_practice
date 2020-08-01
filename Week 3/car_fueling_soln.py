# python3
import sys


def compute_min_refills(distance, tank, ngas, stops):
    
    numRef = 0
    currRef = 0
    # ngas = len(stops) - 2
    
    while currRef <= ngas:
        lastRef = currRef
        while ((currRef <= ngas) and ((stops[currRef+1] - stops[lastRef]) <= tank)) :
            currRef += 1
        if currRef == lastRef:
            return -1
        if currRef <= ngas:
            numRef += 1
        
    return numRef 

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    # d, m, n, *stops = map(int, input().split())
    stops.append(d)
    all_stops = [0]
    for i in range(len(stops)):
        all_stops.append(stops[i])
    
    print(compute_min_refills(d, m, n, all_stops))
