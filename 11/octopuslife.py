from collections import deque


class OctopusLife:
    octopusLevels = None
    flashed = None
    width = None
    heigth = None
    flashes = None


    def __init__(self, lines):
        nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
        width = len(lines[0])
        self.width = width
        height = len(lines)
        self.heigth = height
        self.flashes = 0

        self.octopusLevels = {}
        for i in range(width):
            for j in range(height):
                tmpnb = []
                for (dx, dy) in nb:
                    if 0 <= (i + dx) < width and 0 <= (j + dy) < height:
                        tmpnb.append((i+dx, j+dy))
                self.octopusLevels[(i, j)] = (int(lines[j][i]), tmpnb)


    def do_turn(self):
        already_flashed = set()
        flashed = deque()


        # first pass : +1 everywhere
        for pos in self.octopusLevels:
            (lvl, nbs) = self.octopusLevels[pos]
            lvl += 1
            self.octopusLevels[pos] = (lvl, nbs)
            if lvl > 9:
                flashed.append(pos)
                already_flashed.add(pos)

        while len(flashed)>0:
            oct = flashed.popleft()
            (_, next_oct) = self.octopusLevels[oct]
            for pos in next_oct:
                (lvl, nbs) = self.octopusLevels[pos]
                lvl += 1
                self.octopusLevels[pos] = (lvl, nbs)
                if lvl > 9 and pos not in already_flashed:
                    flashed.append(pos)
                    already_flashed.add(pos)
        for pos in already_flashed:
            (_, nb) = self.octopusLevels[pos]
            self.octopusLevels[pos] = (0, nb)
        self.flashes += len(already_flashed)
        return len(already_flashed)


    def __repr__(self):
        res = ''
        for j in range(self.heigth):
            for i in range(self.width):
                if (i,j) in self.octopusLevels:
                    res += str(self.octopusLevels[(i,j)][0])
                else:
                    res += '.'
            res += '\n'
        return res








