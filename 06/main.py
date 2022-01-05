import cProfile
import logging

from loadValues import LoadValues




def main():
    number = 0

    lv = LoadValues("input")
    lantern = list(lv.comma_list_to_intlist())
    print(lantern)
    days = 80
    curDay = 0
    for curDay in range(days):
        new_fish = lantern.count(0)
        new_lantern = [d-1 if d>0 else 6 for d in lantern]
        new_lantern += [8]* new_fish
        # print(len(new_lantern), new_lantern)
        lantern = new_lantern
        number = len(lantern)


    print("Star 1 : ", number)

    number = 0
    lantern = list(lv.comma_list_to_intlist())
    lantern_fish_count = [0]*9
    for i in range(9):
        lantern_fish_count[i] = lantern.count(i)
    for curDay in range(257):
        print(curDay, sum(lantern_fish_count), lantern_fish_count)
        tmp = lantern_fish_count[0]
        for i in range(8):
            lantern_fish_count[i] = lantern_fish_count[i+1]
        lantern_fish_count[6] += tmp
        lantern_fish_count[8] = tmp


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
