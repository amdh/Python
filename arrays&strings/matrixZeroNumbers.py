
def zero_out(matrix):
    """Given an NxM matrix zero out all rows and columns that contain at least one zero."""
    zero_cols = (i for i, col in enumerate(zip(*matrix)) if ~all(col))
    zero_rows = [i for i, row in enumerate(matrix) if ~all(row)]
    ncol = len(matrix[0])
    for coli in zero_cols:
        for row in matrix:
            row[coli] = 0
    for rowi in zero_rows:
        matrix[rowi] = [0]*ncol

    print(matrix)


matrix = [[5, 3, 2, 1],
                [-3, 0, 5, 0],
                [0, -1, 2, 6]]

zero_out(matrix)


def matrixZero(matrix):
