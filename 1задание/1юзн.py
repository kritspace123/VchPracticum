# Функция для "красивого" вывода матрицы
def printM(A):
    n = len(A)
    for i in range(n):
        print(*A[i], end='\n')

#Функция, определяющая определитель матрицы А
def det(A):
    n = len(A)
    determ = 1
    for i in range(n):
        if(A[i][i] == 0):
            return 0
        determ *= A[i][i]
    return determ


def metod_Gaussa(A):
    # Прямой ход метода Гаусса
    n = len(A)
    # i - номер столбца=строки
    for i in range(n):
        # Поиск максимального элемента в текущем столбце для частичного выбора главного элемента
        max_row = i #номер строки с максимальным элементом в столбце
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        # Обмен строками
        A[i], A[max_row] = A[max_row], A[i]
        # Приведение элемента на главной диагонали к 1
        tem = A[i][i]
        for j in range(i, n+1):
            A[i][j] /= tem

        # Обнуление элементов под главной диагональю
        for j in range(i+1, n):
            factor = A[j][i]
            for k in range(i, n+1):
                A[j][k] -= factor * A[i][k]

    # Обратный ход метода Гаусса
    solution = [0] * n
    for i in range(n-1, -1, -1):
        solution[i] = A[i][n]
        for j in range(i+1, n):
            solution[i] -= A[i][j] * solution[j]

    if(det(A) == 0):
        return None, "Система уравнений вырождена"
    return solution, None

#Драйвер
if __name__ == "__main__":
    with open('test.txt', "r") as f:
        # Cчитываем тест
        A = []
        for line in f:
            A.append([int(x) for x in line.split()])


    solution, error = metod_Gaussa(A)

    if error:
        print(error)
    else:
        print("Решение системы уравнений:")
        for i in range(len(solution)):
            print(f"x{i + 1} = {solution[i]:.2f}")

