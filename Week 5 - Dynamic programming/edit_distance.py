# Uses python3
def edit_distance(s, t):
    #write your code here
    m, n = len(s), len(t)
    distances = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                distances[i][j] = j
            elif j == 0:
                distances[i][j] = i
            elif s[i-1] == t[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else: 
                minval = min(
                    distances[i][j-1], 
                    distances[i-1][j],
                    distances[i-1][j-1]
                    )
                distances[i][j] = 1 + minval

    return distances[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
