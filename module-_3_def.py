def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix_1 = []
        for j in range(0, m):
            matrix_1.append(value)
        matrix.append(matrix_1)
    return matrix

result_1 = get_matrix(3,2,56)
result_2 = get_matrix(4,4,15)
result_3 = get_matrix(2,5,3)
print(result_1)
print(result_2)
print(result_3)