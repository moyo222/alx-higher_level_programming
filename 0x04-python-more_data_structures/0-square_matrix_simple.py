#!/usr/bin/python3
<<<<<<< HEAD
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)

=======

def square_matrix_simple(matrix=[]):

    new_matrix = matrix.copy()


    for i in range(len(matrix)):

        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

return (new_matrix)
>>>>>>> 457447308eb1857af3a709045dc7fe7d889f4b1e
