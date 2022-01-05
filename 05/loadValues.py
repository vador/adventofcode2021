import re


def parse_direction(element):
    (direction, quantity) = element.strip().split(" ")
    return direction, int(quantity)


class LoadValues:
    file = 'input'
    raw_values = None
    processed_values = None

    def __init__(self, data=None, file=True, groups=False):
        if file:
            if data is not None:
                file_name = data
            else:
                file_name = self.file
            if groups:
                with open(file_name) as f:
                    self.raw_values = [line.split('\n') for line in f.read().strip().split("\n\n")]
            else:
                with open(file_name) as f:
                    self.raw_values = list(f)
        else:
            self.raw_values = list(data)

    def get_groups_from_lines(self, raw=None):
        if raw is None:
            raw = self.raw_values
        raw = self.strip_lines(raw)
        groups = []
        tmpgroup = []
        for line in raw:
            if len(line) >= 1:
                tmpgroup.append(line)
            else:
                groups.append(tmpgroup)
                tmpgroup = []
        if len(tmpgroup) >= 1:
            groups.append(tmpgroup)
        self.processed_values = groups
        return groups

    def list_to_intlist(self, raw=None):
        if raw is None:
            raw = self.raw_values
        self.processed_values = [int(val) for val in raw]
        return self.processed_values

    def comma_list_to_intlist(self, raw=None):
        if raw is None:
            raw = self.raw_values
        self.processed_values = raw[0].split(",")
        return self.processed_values

    def get_2d_coords_pairs(self, raw=None):
        tmpRes = []
        if raw is None:
            raw = self.raw_values
        for ln in raw:
            coords = ln.split(' -> ')
            start = list(map(int, coords[0].split(',')))
            end = list(map(int, coords[1].split(',')))
            tmpRes.append(((start[0], start[1]), (end[0], end[1])))
        return tmpRes

    def get_3d_coords(self, raw=None):
        if raw is None:
            raw = self.raw_values
        coords = [tuple(map(int, list(re.findall(r'-?\d+', ln)))) for ln in raw]
        self.processed_values = coords
        return coords

    def get_directions(self, raw=None):
        directions = []
        if raw is None:
            raw = self.raw_values
        for ln in raw:
            (direction, qty) = parse_direction(ln)
            directions.append((direction, qty))
        return directions

    def get_digit_list(self, raw=None):
        if raw is None:
            raw = self.raw_values
        tmp = str(raw[0]).strip()
        return [int(i) for i in list(tmp)]

    def get_bits(self, raw=None):
        res = []
        if raw is None:
            raw = self.raw_values
        for ln in raw:
            tmp = str(ln).strip()
            res.append([int(i) for i in list(tmp)])
        return res

    def strip_lines(self, raw=None):
        if raw is None:
            raw = self.raw_values
        tmp = [line.strip() for line in raw]
        self.processed_values = tmp
        return tmp


if __name__ == '__main__':
    lv = LoadValues("input")

    print(lv.strip_lines())
