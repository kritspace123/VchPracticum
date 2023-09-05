import random
from random import randint


with open('test.txt', "w") as f:
    # Генерируем ранг матрицы
    n = random.randint(3, 5)

    #Создаём матрицу коэф.
    a = [[randint(1, 100) for j in range(n)] for i in range(n)]

    #Находим матрицу свободных членов
    b = [0] * n
    c = 0
    for i in range(n):
        for j in range(n):
            c += a[i][j]
        b[i] = c

    #записываем массив в файл
    print(n, file=f)
    for i in range(n):
        print(*a[i], file=f)
    print(*b, file=f)
