# Функция для "красивого" вывода матрицы
def printM(A):
    n = len(A)
    for i in range(n):
        print(*A[i], end='\n')

def unit_matrix(n):
    E = [[0]*n]*n
    for i in range(n):
        E[i][i] = 1
    return E
def m_multiplication(A, b):
    if len(A[0]) != len(b):
        return "Нельзя умножить матрицу на вектор. Количество столбцов матрицы не равно количеству элементов вектора.", None
    result = [sum(A[i][k] * b[k] for k in range(len(b))) for i in range(len(A))]
    return None, result

# Напишем драйвер
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

    error, C = m_multiplication(A, b)
    if(error != None):
        print(error)


