import cProfile
import logging

from loadValues import LoadValues

from collections import defaultdict, deque

class Field:
    pointlist = None

    def __init__(self, plist):
        self.pointlist = plist.copy()

    def fold_x(self, fold_pos):
        new_pointlist = set()
        for (x,y) in self.pointlist:
            if x > fold_pos:
                x = fold_pos - (x - fold_pos)
            new_pointlist.add((x,y))
        self.pointlist = new_pointlist
        return len(self.pointlist)

    def fold_y(self, fold_pos):
        new_pointlist = set()
        for (x,y) in self.pointlist:
            if y > fold_pos:
                y = fold_pos - (y - fold_pos)
            new_pointlist.add((x,y))
        self.pointlist = new_pointlist
        return len(self.pointlist)

    def fold(self, parm):
        (axis, pos) = parm
        if axis == 'x':
            res = self.fold_x(pos)
        else:
            res = self.fold_y(pos)
        return res

    def __repr__(self):
        xmax = max([x for (x,y) in self.pointlist])+1
        ymax = max([y for (x,y) in self.pointlist])+1
        res = ''
        for j in range(ymax):
            for i in range(xmax):
                if (i,j) in self.pointlist:
                    res += '#'
                else:
                    res += '.'
            res += '\n'
        return res






def main():
    number = 0

    lv = LoadValues("input")
    data = lv.strip_lines()

    point_list = []
    fold_list = []
    still_points = True
    for line in data:
        if line == '':
            still_points = False
        elif still_points:
            (x,y) = list(map(int,line.split(',')))
            point_list.append((x,y))
        else:
            (xy, pos) = line.split('=')
            xy = xy[-1]
            pos = int(pos)
            fold_list.append((xy, pos))

    print(point_list)
    print(fold_list)
    ff = Field(point_list)
    # print(ff)


    number = ff.fold(fold_list[0])

    print(ff)
    print("Star 1 : ", number)

    ff = Field(point_list)
    for parm in fold_list:
        ff.fold(parm)

    print(ff)

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
