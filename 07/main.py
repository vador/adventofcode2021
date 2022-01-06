import cProfile
import logging

from loadValues import LoadValues


def fuel_cost_constant(pos, crab_positions):
    return sum([abs(pos - crab) for crab in crab_positions])


def fuel_cost_linear(pos, crab_positions):
    tmp = [abs(pos - crab) * (abs(pos - crab) + 1) // 2 for crab in crab_positions]
    return sum(tmp)


def main():
    number = 0

    lv = LoadValues("input")
    crabs = list(lv.comma_list_to_intlist())

    min_pos = min(crabs)
    max_pos = max(crabs)
    best_fuel = sum(crabs)
    for pos in range(min_pos, max_pos + 1):
        cur_fuel = fuel_cost_constant(pos, crabs)
        if cur_fuel < best_fuel:
            best_fuel = cur_fuel

    number = best_fuel
    print("Star 1 : ", number)

    number = 0
    min_pos = min(crabs)
    max_pos = max(crabs)
    best_fuel = sum(crabs) * sum(crabs)
    for pos in range(min_pos, max_pos + 1):
        cur_fuel = fuel_cost_linear(pos, crabs)
        if cur_fuel < best_fuel:
            best_fuel = cur_fuel

    number = best_fuel

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
