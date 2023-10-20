import random

def generate_2d(rows, cols):
    matrix = []
    for _ in range(rows):
        matrix_row = []
        for _ in range(cols):
            matrix_row.append(random.randint(1,100))
        
        matrix.append(matrix_row)
    return matrix

matrix_2d = generate_2d(5,8)

for row in range(len(matrix_2d)):
    print(matrix_2d[row])
