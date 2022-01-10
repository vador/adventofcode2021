import cProfile
import logging

from loadValues import LoadValues

from collections import defaultdict, deque

def trace(map, dbls):
    ct = 0
    tracker = deque([("start", set(["start"]), False)])
    while tracker:
        p, seen, visited = tracker.popleft()
        if p == "end":
            ct += 1
            continue
        for c in map[p]:
            if c not in seen:
                seen_cp = set(seen)
                if c.islower():
                    seen_cp.add(c)
                tracker.append((c, seen_cp, visited))
            elif c in seen and not visited and c not in ["start", "end"] and dbls:
                tracker.append((c, seen, c))
    return ct


def main():
    number = 0

    lv = LoadValues("input")
    data = lv.strip_lines()

    map = defaultdict(list)
    for line in data:
        p, c = line.split("-")
        map[p].append(c)
        map[c].append(p)

    number = trace(map, False)
    print("Star 1 : ", number)


    number = 0
    number = trace(map, True)



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
    pr.print_stats()
