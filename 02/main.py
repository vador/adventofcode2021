import logging
import cProfile
from loadValues import LoadValues




def main():
    number = 0

    lv = LoadValues("input")
    lines = lv.strip_lines()
    directions = lv.get_directions()

    print(directions)
    depth = 0
    hposition = 0
    for (direction, qty) in directions:
        if direction == "forward":
            hposition += qty
        elif direction == "down":
            depth += qty
        else:
            depth -= qty

    print(hposition, depth)
    number = hposition * depth
    print("Star 1 : ", number)

    number = 0
    depth = 0
    hposition = 0
    aim = 0
    for (direction, qty) in directions:
        if direction == "forward":
            hposition += qty
            depth += aim * qty
        elif direction == "down":
            aim += qty
        else:
            aim -= qty
    print(hposition, depth)
    number = hposition * depth

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
