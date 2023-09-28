import copy


def Print_m(A):
    for i in range(len(A)):
        print(*A[i])
    print('\n')

def multiply(P, T):
    n = len(P)  # Определите 'n' здесь
    result = [[0] * n for _ in range(n)]
    for i in range(len(P)):
        for j in range(len(P)):
            for k in range(len(P)):
                result[i][j] += P[i][k] * T[k][j]
    return result
def Q(A, k, l):
    n = len(A)
    #вычисляем синус и косинус
    e =((A[k][k] ** 2) + (A[l][k] ** 2) ) ** (1/2)
    s = ((-1) * A[l][k]) / e
    c = (A[k][k]) / e

    VEr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                if(i != k) and (i != l):
                    VEr[i][j] = 1
                else:
                    if(i == k or i == l):
                        VEr[i][j] = c
            elif i == k and j == l:
                VEr[i][j] = -1 * s
            elif i == l and j == k:
                VEr[i][j] = s
    return VEr


def vrasheniya(A):

    for k in range(1, len(A)-1):
        for l in range(k+1, len(A)):
            Print_m(Q(A, 0, 1))
            Print_m(multiply(Q(A, 0, 1), A))
            Print_m(Q(A, 0, 2))
            Print_m(multiply(Q(A, 0, 2), A))



if __name__ == "__main__":
    # Cчитываем тест
    with open('task1.txt', "r") as f:
        A = []
        li = f.readline()
        n = len(li)
        A.append([float(x) for x in li.split()])
        n = len(A[0])
        cou = 1
        for line in f:
            A.append([float(x) for x in line.split()])
            cou += 1
            if(cou == n):
                break
        li = f.readline()
        b = []
        for x in li.split():
            b.append([float(x)])
    k = 0
    l = 1
    # Print_m(A)
    n = len(A)
    vrasheniya(A)
    Q(A, 0, 1)
