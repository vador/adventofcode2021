import logging
import cProfile
from loadValues import LoadValues

from operator import add

def displayField(localfield):
    mx = 0
    my = 0
    for (i,j) in localfield:
        mx = max(i, mx)
        my = max(j, my)
    for j in range(my+1):
        for i in range(mx+1):
            if (i, j) in localfield:
                res = str(localfield[(i, j)])
            else:
                res = '.'
            print(res, " ", end='')
        print()


def getCoordListForLine(start, end, diagonal=False):
    (x1, y1) = start
    (x2, y2) = end
    line = []

    if (x1 == x2) or (y1 == y2):
        (a, b) = (x1, x2)
        (a, b) = (min(a, b), max(a, b))
        for i in range(a, b + 1):
            (a, b) = (y1, y2)
            (a, b) = (min(a, b), max(a, b))
            for j in range(a, b + 1):
                line.append((i,j))
    elif diagonal:
        if x2 < x1:
            (x1, y1) = end
            (x2, y2) = start
        if y1 > y2:
            incr = -1
        else:
            incr = 1
        for i in range(x2-x1+1):
            line.append((x1+i, y1+(incr*i)))

    return line


def main():
    number = 0

    lv = LoadValues("input")
    coords = lv.get_2d_coords_pairs()
    field = {}

    for (start, end) in coords:
        for coord in getCoordListForLine(start, end):
            if coord in field:
                field[coord] += 1
            else:
                field[coord] = 1

    for k in field:
        if (field[k]>1):
            number +=1
    # displayField(field)

    print("Star 1 : ", number)

    number = 0
    field = {}
    for (start, end) in coords:
        print((start, end), getCoordListForLine(start, end, diagonal=True))
        for coord in getCoordListForLine(start, end, diagonal=True):
            if coord in field:
                field[coord] += 1
            else:
                field[coord] = 1
    # displayField(field)

    for k in field:
        if (field[k] > 1):
            number += 1

    print("Star 2 : ", number)



##
if __name__ == '__main__':
    pr = cProfile.Profile()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Started')
    pr.enable()
    main()
    pr.disable()

    logging.info('Finished')
    # pr.print_stats()
