import numpy as np

def rotation_matrix(a, b):
    """
    Создает матрицу вращения для обнуления элемента b с использованием элемента a.
    """
    r = np.sqrt(a**2 + b**2)
    c = a / r
    s = b / r
    rotation = np.array([[c, -s],
                         [s, c]])
    return rotation

def upper_triangularize(matrix):
    """
    Приводит матрицу к верхнетреугольному виду с использованием матриц вращения.
    """
    m, n = matrix.shape
    for j in range(min(m, n)):  # Добавляем проверку на минимум из m и n
        for i in range(j + 1, m):
            if matrix[i, j] != 0:
                a = matrix[j, j]
                b = matrix[i, j]
                rotation = rotation_matrix(a, b)
                matrix[[j, i], :] = np.dot(rotation, matrix[[j, i], :])
    return matrix

# Пример использования
matrix = np.array([[3, 2, -1],
                  [2, -1, 5],
                  [1, 7, -1]], dtype=float)

result = upper_triangularize(matrix)
print(result)