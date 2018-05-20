import numpy as np


def input_int(output, check = 2):
    try:
        while(True):
         n = int(input(output))
         if n >= check:
             return n
    except ValueError:
        print('Incorrect number. Please input int number next time.')
        exit(-1)

if __name__ == "__main__":
    n = input_int('Input count of nodes: ')

    A = np.random.randint(0, 2, size = (n,n))

    for i in range(len(A)):
        A[i][i] = 0

    print('Matrix :\n', A)

    length = input_int('Input length: ')

    temp_matrix = np.copy(A)

    for i in range(length - 1):
        A = np.matmul(A, temp_matrix)

    #print("Matrix^{0}:\n".format(length), A)

    node_number = input_int('Input number node`s number:', 1)

    print("Circles count of node #{0}: ".format(node_number), A[node_number - 1][node_number - 1])

    input("Press any key to close application")
