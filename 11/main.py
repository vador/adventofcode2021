import cProfile
import logging

from loadValues import LoadValues
from octopuslife import OctopusLife



def main():
    number = 0

    lv = LoadValues("input")
    lines = lv.strip_lines()

    ol = OctopusLife(lines)
    print(ol.octopusLevels)

    print(ol)

    for i in range(100):
        print("Step ", i+1)
        nb = ol.do_turn()
        print(ol)
        print("Flashes:" , nb)
        print("T Flash:", ol.flashes)
    number = ol.flashes

    print("Star 1 : ", number)

    ol = OctopusLife(lines)
    number = 0
    ttflash = ol.width * ol.heigth

    number = 0

    fl = 0
    while fl < ttflash:
        number +=1
        fl = ol.do_turn()
        print(number, fl)



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
