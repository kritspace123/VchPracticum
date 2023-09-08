# Функция для "красивого" вывода матрицы
def printM(A):
    n = len(A)
    for i in range(n):
        print(*A[i], end='\n')


def get_A_minor(A, row, col):
    return [row[:col] + row[col+1:] for row in (A[:row] + A[row+1:])]

def calculate_determinant(A):
    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    determinant = 0
    for col in range(len(A)):
        determinant += ((-1) ** col) * A[0][col] * calculate_determinant(get_A_minor(A, 0, col))
    return determinant

def det(A):
    n = len(A[0])-1
    determ = 1
    for i in range(n):
        if(A[i][i] == 0):
            return 0
        determ *= A[i][i]
    return determ

def Gauss_method(A):
    n = len(A[0])-1
    # Прямой ход метода Гаусса
    cou = 0
    m = 1
    for i in range(n):
        # Поиск максимального элемента в столбце i и перестановка строк
        max_row = i

        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        if( max_row != i):
            cou = cou + 1

        # Деление текущей строки на главный элемент
        divider = A[i][i]
        m = m * divider
        if divider == 0:
            raise Exception("Метод Гаусса не применим: деление на ноль")
        for j in range(i, n+1):
            A[i][j] /= divider

        # Вычитание текущей строки из всех нижних строк
        for j in range(i + 1, n):
            factor = A[j][i] * (-1)
            for k in range(i, n+1):
                A[j][k] += factor * A[i][k]
    if (det(A) == 0):
        raise Exception("Метод Гаусса не применим: деление на ноль")
    print((det(A) * ((-1)**cou)) * m)
    # Обратный ход метода Гаусса
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = A[i][n]
        for j in range(i + 1, n):
            solution[i] -= A[i][j] * solution[j]
        solution[i] /= A[i][i]

    return solution

#Драйвер
if __name__ == "__main__":
    with open('../1задание/test.txt', "r") as f:
        # Cчитываем тест
        A = []
        for line in f:
            A.append([float(x) for x in line.split()])

    solution = Gauss_method(A)
    cou = 0
    print("Решение системы уравнений:")
    for i in solution:
        cou +=1
        print(f"x{cou} = {i:.5f}")