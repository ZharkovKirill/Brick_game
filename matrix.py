#Матрица создается путем замешиваня изначально решенной
#Используется специальное замешивание формой буквой Г
#Оно вносит больше хаоса чем простой рандом
import numpy as np
import random
def zero(field):
    zeros = []
    for i in range(0, 5):
        for j in range(0, 5):
            if (field[i][j] == 0):
                zeros.append([i, j])
    return zeros
def fluct(a,b):
    a1 = np.array(a)
    b1 = np.array(b)
    a1 -=b1
    sum = 0
    for i in a1.flat:
        if(i!=0):
            sum+=1
    return sum
def tsun(field, zeros):
    random.seed()
    random.shuffle(zeros)
    ways1 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    random.shuffle(ways1)
    for i in range(len(zeros) - 1):
        y = zeros[i][0]
        x = zeros[i][1]
        for j in ways1:
            if ((y + j[0]) != -1) and ((x + j[1]) != 5):
                if ((x + j[1]) != -1) and ((y + j[0]) != 5):
                    if (field[y + j[0]][x+ j[1]] > 1):
                        x +=j[1]
                        y +=j[0]
                        ways1.remove(j)
                        for k in ways1:
                                if ((x + k[1]) !=  -1) and ((y + k[0]) !=  5):
                                    if ((y + k[0]) !=  -1) and ((x + k[1]) !=  5):
                                        if (field[y + k[0]][x + k[1]] > 1):
                                            field[y][x], field[zeros[i][0]][zeros[i][1]] = field[zeros[i][0]][zeros[i][1]],field[y][x]
                                            field[y][x], field[y + k[0]][x + k[1]] = field[y + k[0]][x + k[1]], field[y][x]
                                            zeros[i] = [y + k[0], x + k[1]]
                                            return 0
def field_ini():
    a = [
        [2, 1, 3, 1, 4],
        [2, 0, 3, 0, 4],
        [2, 1, 3, 1, 4],
        [2, 0, 3, 0, 4],
        [2, 1, 3, 1, 4]
    ]
    a[:3] = np.random.permutation(a[:3])
    a[:1] = np.random.permutation(a[:1])
    while (1):
        a1 = np.array(a)
        zerous = zero(a1)
        b = np.array(a)

        for i in range(600):
            tsun(a1,zerous)
        if(fluct(a1,b)>13):
            print(fluct(a1, b))
            print(a1)
            break
    return  a1

if __name__ == "__main__":
    field_ini()
