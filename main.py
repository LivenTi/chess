from random import randint

forbid = []
bishops = []


def get_all_squares(square):
    local_forbid = [square]
    for i in range(1, 8):
        diag = [square[0] - i, square[1] - i]
        if (diag[0] >= 0) and (diag[1] >= 0):
            local_forbid.append(diag)

        diag = [square[0] - i, square[1] + i]
        if (diag[0] >= 0) and (diag[1] <= 7):
            local_forbid.append(diag)

        diag = [square[0] + i, square[1] - i]
        if (diag[0] <= 7) and (diag[1] >= 0):
            local_forbid.append(diag)

        diag = [square[0] + i, square[1] + i]
        if (diag[0] <= 7) and (diag[1] <= 7):
            local_forbid.append(diag)

    return local_forbid


def add_bishop():
    coords = [randint(0, 7), randint(0, 7)]
    while coords in forbid:
        coords = [randint(0, 7), randint(0, 7)]
    bishops.append(coords)
    forbid.extend(get_all_squares(coords))


for i in range(8):
    add_bishop()

a = [[0 for j in range(8)] for i in range(8)]

for sq in bishops:
    a[sq[0]][sq[1]] = 1

for i in range(8):
    print(a[i])
