import test
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
from timeit import default_timer as timer


def __exp__():
    n = input("Inserire numero di vertici iniziale: ")
    max = input("Inserire numero di vertici finale ")
    increase = input("Inserire incremento tra i test: ")
    p = max
    x = []
    y = []
    while n <= max:
        #x.append(n)
        matrix = [[0 for i in range(0, n)] for j in range(0, n)]
        for i in range(0, n):
            for j in range(0, n):
                value = random.randint(0, max)
                if value > p and i != j:
                    matrix[i][j] = 1
        #    print str(matrix[i])
        start = timer()
        test.test(matrix)
        end = timer()
        y.append(end-start)
        n += increase
        p -= 1
        print " "
    #plt.plot(x,y)
    #plt.show()


if __name__ == __exp__():
    __exp__()
