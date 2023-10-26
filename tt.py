def jacobi_iteration(A, b, max_iterations, tol):
    n = len(A)
    x = [0.0] * n  # Начальное приближение к решению
    x_new = [0.0] * n  # Место для хранения нового приближения

    for iteration in range(max_iterations):
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        # Проверка на сходимость по достижении заданной точности
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new.copy()

    return x

if __name__ =="__main__":

    # Считываем матрицу из файла
    with open("input.txt") as f:
        A = []
        n = int(f.readline()) #считываем размерность матрицы А
        for i in range(n):
            line = f.readline()
            A.append([float(x) for x in line.split()])
        line = f.readline()
        b = [float(x) for x in line.split()]

    # Пример использования
    max_iterations = 100
    tolerance = 1e-6

    result = jacobi_iteration(A, b, max_iterations, tolerance)
    print("Решение:", result)





