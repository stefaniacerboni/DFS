import random
import test
def __main__():
    n = input("Insert n elements: ")

    matrix = [[0 for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            value = random.randint(0, n)
            if value > (n-1) and i != j:
                matrix[i][j] = 1
    for i in range(0, n):
        print str(matrix[i])
    test.test(matrix)

if __name__==__main__():
    __main__()