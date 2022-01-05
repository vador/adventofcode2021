import logging
import cProfile
from loadValues import LoadValues

from operator import add



def main():
    number = 0

    lv = LoadValues("input")
    lines = lv.strip_lines()

    bits = lv.get_bits()

    number = get_consumption(bits)
    print("Star 1 : ", number)

    number = 0

    bits = lv.get_bits()

    for pos in range(len(bits[0])):
        bits = scrub_list_o2(bits, pos)

    o2_rating = ''.join(map(str,bits[0]))
    o2 = int(o2_rating, 2)

    print(o2_rating, o2)

    bits = lv.get_bits()

    for pos in range(len(bits[0])):
        bits = scrub_list_co2(bits, pos)
    co2_rating = ''.join(map(str,bits[0]))
    co2 = int(co2_rating, 2)
    print(co2_rating, co2)

    number = o2*co2

    print("Star 2 : ", number)


def get_consumption(bits):
    nblines = len(bits)
    ones = [0 for i in bits[0]]
    for ln in bits:
        ones = list(map(add, ones, ln))
    gamma_bits = ''.join([str(int(x > nblines / 2)) for x in ones])
    epsilon_bits = ''.join([str(int(x < nblines / 2)) for x in ones])
    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)
    print(gamma, epsilon)
    number = gamma * epsilon
    return number

def scrub_list_o2(bits, pos):
    nblines = len(bits)
    if nblines == 1:
        return bits
    ones = 0
    for ln in bits:
        ones = ones + ln[pos]
    keep = (ones >= (nblines/2))
    res = []
    for ln in bits:
        if ln[pos] == keep:
            res.append(ln)
    return res

def scrub_list_co2(bits, pos):
    nblines = len(bits)
    if nblines == 1:
        return bits
    ones = 0
    for ln in bits:
        ones = ones + ln[pos]
    keep = (ones < (nblines/2))
    res = []
    for ln in bits:
        if ln[pos] == keep:
            res.append(ln)
    return res

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
