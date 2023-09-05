with open('test.txt', "r") as f:
    # Cчитываем тест
    n = int(f.readline())
    A = []
    cou = 0
    for line in f:
        if(cou == n):
            break
        A.append([int(x) for x in line.split()])
        cou += 1
    b = ([int(x) for x in line.split()])

    #переходим к верхне-диагональной матрице
    for i in range(n-1):
        for j in range(i+1, n):
            c = (A[j][i])/(A[i][i])
            for t in range(i, n):
                A[j][t] -= c * A[i][t]
                b[j] -= c * b[i]

    # Проверяем определитель
    det = 1
    for i in range(n):
        det = det * A[i][i]
    if(det == 0):
        print("Определитель равен нулю...")
        exit(000)



    for i in range(n):
        print(*A[i])
