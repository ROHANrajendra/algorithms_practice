
import numpy
import math

# Uses python3

class Paranthesizer:
    
    def __init__(self, dataset):

        self.dataset = dataset


    def evalt(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False

    def exp_gen(self, m, M, op, i, j):
        temp_max = -math.inf
        temp_min = math.inf
        for k in range(i,j):
            a = self.evalt(M[i][k], m[k+1][j], op[k])
            b = self.evalt(m[i][k], m[k+1][j], op[k])
            c = self.evalt(M[i][k], M[k+1][j], op[k])
            d = self.evalt(m[i][k], M[k+1][j], op[k])
            temp_min = min(temp_min, a, b, c, d)
            temp_max = max(temp_max, a, b, c, d)
        return (temp_min, temp_max)

    def get_maximum_value(self):
        opr = self.dataset[1:len(self.dataset):2]
        num = self.dataset[0:len(self.dataset) + 1:2]
        n = len(num)
        m = numpy.zeros(shape=(n, n), dtype=int)
        M = numpy.zeros(shape=(n, n), dtype=int)
        for i in range(n):
            m[i][i] = int(num[i])
            M[i][i] = int(num[i])
        for i in range(1,n):
            for j in range(n-i):
                s = i + j
                m[j][s], M[j][s] = self.exp_gen(m, M, opr, j, s)
        
        return M[0][n-1]


if __name__ == "__main__":
    maximized_expression = Paranthesizer(input())
    print(maximized_expression.get_maximum_value())
