import numpy as np


class StrRepresentationMixin:
    def __str__(self):
        return "[[" + "],\n[".join([", ".join(map(str, row)) for row in self.matrix]) + "]]"


class WriteFileMixin:
    def write_to_file(self, path):
        with open(path, 'w') as f:
            f.write(str(self))


class PropertyMixin:
    def __init__(self, matrix_val):
        self.matrix = np.asarray(matrix_val)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix


class MatrixMixins(
    np.lib.mixins.NDArrayOperatorsMixin,
    StrRepresentationMixin,
    WriteFileMixin,
    PropertyMixin
):

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        for x in inputs:
            if not isinstance(x, MatrixMixins):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x.matrix for x in inputs)
        return MatrixMixins(getattr(ufunc, method)(*inputs, **kwargs))



