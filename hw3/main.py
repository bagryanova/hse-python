import os
import numpy as np
from matrix import Matrix
from matrix_mixins import MatrixMixins


def get_easy_artifacts():
    if not os.path.exists('artifacts/easy'):
        os.mkdir('artifacts/easy')

    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    '''matrix1 = Matrix([
        [1, 2],
        [4, 5]
    ])

    matrix2 = Matrix([
        [7,8],
        [9, 1],
        [2, 3]
    ])'''
    res = matrix1 + matrix2
    with open('artifacts/easy/matrix+.txt', 'w') as f:
        f.write(res.__str__())

    res = matrix1 * matrix2
    with open('artifacts/easy/matrix*.txt', 'w') as f:
        f.write(res.__str__())

    res = matrix1 @ matrix2
    with open('artifacts/easy/matrix@.txt', 'w') as f:
        f.write(res.__str__())


def get_medium_artifacts():
    if not os.path.exists('artifacts/medium'):
        os.mkdir('artifacts/medium')

    np.random.seed(0)
    matrix1 = MatrixMixins(np.random.randint(0, 10, (10, 10)))
    matrix2 = MatrixMixins(np.random.randint(0, 10, (10, 10)))

    '''matrix1 = MatrixMixins([
        [1, 2],
        [4, 5]
    ])

    matrix2 = MatrixMixins([
        [7,8],
        [9, 1],
        [2, 3]
    ])'''

    res = matrix1 + matrix2
    with open('artifacts/medium/matrix+.txt', 'w') as f:
        f.write(res.__str__())

    res = matrix1 * matrix2
    with open('artifacts/medium/matrix*.txt', 'w') as f:
        f.write(res.__str__())

    res = matrix1 @ matrix2
    with open('artifacts/medium/matrix@.txt', 'w') as f:
        f.write(res.__str__())


def get_hard_artifacts():
    if not os.path.exists('artifacts/hard'):
        os.mkdir('artifacts/hard')

    a = Matrix([
        [0, 0],
        [0, 0]
    ])
    c = Matrix([
        [50, 50],
        [50, 49]
    ])
    b = Matrix([
        [1, 1],
        [1, 1]
    ])
    d = Matrix([
        [1, 1],
        [1, 1]
    ])

    with open('artifacts/hard/A.txt', 'w') as f:
        f.write(a.__str__())
    with open('artifacts/hard/B.txt', 'w') as f:
        f.write(b.__str__())
    with open('artifacts/hard/C.txt', 'w') as f:
        f.write(c.__str__())
    with open('artifacts/hard/D.txt', 'w') as f:
        f.write(d.__str__())
    #print(hash(a), hash(c))

    cur = a @ b
    res = "Hash AB:" + str(hash(cur)) + "\n"
    with open('artifacts/hard/AB.txt', 'w') as f:
        f.write(cur.__str__())
    #print(c @ d)
    Matrix.clean_cache()
    cur = c @ d
    res += "Hash CD:" + str(hash(cur)) + "\n"
    with open('artifacts/hard/CD.txt', 'w') as f:
        f.write(cur.__str__())

    with open('artifacts/hard/hash.txt', 'w') as f:
        f.write(res.__str__())


if __name__ == '__main__':
    if not os.path.exists('artifacts'):
        os.mkdir('artifacts')

    get_easy_artifacts()
    get_medium_artifacts()
    get_hard_artifacts()
