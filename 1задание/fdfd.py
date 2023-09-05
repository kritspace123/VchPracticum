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


def Gauss_method(A):
    n = len(A)
    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск максимального элемента в столбце i и перестановка строк
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]

        # Деление текущей строки на главный элемент
        divider = A[i][i]
        if divider == 0:
            raise Exception("Метод Гаусса не применим: деление на ноль")
        for j in range(i, n+1):
            A[i][j] /= divider

        # Вычитание текущей строки из всех нижних строк
        for j in range(i + 1, n):
            factor = A[j][i]
            for k in range(i, n+1):
                A[j][k] -= factor * A[i][k]


    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x


#Драйвер
if __name__ == "__main__":
    with open('test.txt', "r") as f:
        # Cчитываем тест
        A = []
        for line in f:
            A.append([int(x) for x in line.split()])


    solution = Gauss_method(A)
    cou = 0
    print(solution)
    print("Решение системы уравнений:")
    for i in solution:
        cou +=1
        print(f"x{cou} = {i:.2f}")