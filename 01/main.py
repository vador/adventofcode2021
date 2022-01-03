import logging
import cProfile
from loadValues import LoadValues




def main():
    number = 0

    lv = LoadValues("input")
    lines = lv.strip_lines()
    keyList = lv.list_to_intlist()

    number = 0
    curKey = keyList[0]
    for key in keyList:
        if key > curKey:
            number += 1
        curKey = key


    print("Star 1 : ", number)

    sliding = []
    for i in range(len(keyList) - 2):
        sliding.append(keyList[i] + keyList[i+1] + keyList[i+2])

    print(sliding)
    number = 0
    curKey = sliding[0]
    for key in sliding:
        if key > curKey:
            number += 1
        curKey = key

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
