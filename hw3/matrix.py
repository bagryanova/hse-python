import numpy as np


class HashMixin:
    def __hash__(self):
        """Sum of all elements in matrix modulo 199"""

        res = 0
        for row in self.matrix:
            res += np.sum(row)
        return int(res % 199)


class Matrix(HashMixin):
    _matmul_cache = {}

    @staticmethod
    def clean_cache():
        Matrix._matmul_cache = {}

    def __init__(self, matrix_val):
        self._check_matrix(matrix_val)
        res = []
        for row in matrix_val:
            res.append(row)
        self.matrix = res
        self.shape = len(matrix_val), len(matrix_val[0])

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, shape):
        self._shape = shape

    @staticmethod
    def _check_matrix(matrix):
        if len(matrix) == 0:
            raise ValueError("Matrix length can not be zero")
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError("Rows of the matrix must have the same length")

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrix sizes should be the same")
        res = Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        return res

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrix sizes should be the same")
        res = Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(self._shape[1])] for i in range(self.shape[0])])
        return res

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Can not multiply matrix with such size")

        key = hash(self), hash(other)
        if key in Matrix._matmul_cache:
            return Matrix._matmul_cache[key]

        res = Matrix([[
            np.sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.shape[1])])
            for j in range(other.shape[1])]
            for i in range(self.shape[0])
        ])
        Matrix._matmul_cache[key] = res
        return res

    def __str__(self):
        return "[[" + "],\n[".join([", ".join(map(str, row)) for row in self._matrix]) + "]]"


