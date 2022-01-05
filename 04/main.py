import logging
import cProfile
from loadValues import LoadValues
from board import Board

from operator import add


def main():
    number = 0

    lv = LoadValues("input", groups=True)

    print(lv.raw_values)
    numbers = map(int, lv.comma_list_to_intlist(lv.raw_values[0]))

    boards = [Board(line) for line in lv.raw_values[1:]]


    for num in numbers:
        for (i,board) in enumerate(boards):
            res = board.drawNumber(num)
            if res:
                number = res*num
                break
        if number>0:
            break


    print("Star 1 : ", number)

    number = 0
    boards = [Board(line) for line in lv.raw_values[1:]]

    numbers = map(int, lv.comma_list_to_intlist(lv.raw_values[0]))

    numbers = list(numbers)
    while boards:
        num = numbers.pop(0)
        remove = []
        for (i, board) in enumerate(boards):
            res = board.drawNumber(num)
            if res:
                print(i, res, num)
                number = res * num
                boards[i] = None
        boards = [board for board in boards if board is not None]

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
