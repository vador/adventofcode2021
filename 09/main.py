import cProfile
import logging

from loadValues import LoadValues
from field import Field

def main():
    number = 0

    lv = LoadValues("input")
    field = lv.strip_lines()
    ff = Field(field)

    print(ff.field)
    low = ff.return_min_points()
    print("low1 :", low)
    number = sum([h+1 for (pos,h) in low])
    print(number)
    low = ff.return_min_points_neighbors()
    print("low2 :", low)
    number = sum([h+1 for (pos,h) in low])

    print("Star 1 : ", number)

    number = 0
    res = (ff.connected_fields())[:3]
    print(res)
    number = res[0]*res[1]*res[2]
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
