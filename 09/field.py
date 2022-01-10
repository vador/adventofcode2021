import cProfile

class UF:
    c_id = None
    graph = None
    count = None

    def __init__(self, graph):
        self.c_id = {}
        self.graph = graph
        for val in self.graph:
            self.c_id[val] = val
        self.count = len(self.c_id)

    def connected(self, p ,q):
        return self.find(p) == self.find(q)

    def find(self,p):
        return self.c_id[p]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)

        if (p_id == q_id):
            return

        for val in self.c_id:
            if self.c_id[val] == p_id:
                self.c_id[val] = q_id
        self.count -= 1
        return


    def solve(self):
        output = []
        for p in self.graph:
            (_, neigh) = self.graph[p]
            for q in neigh:
                if not (self.connected(p, q)):
                    self.union(p, q)
                    output.append((p, q))
        return self.c_id

    def basin_sizes(self):
        sizes = {}
        for val in self.c_id.values():
            if val in sizes:
                sizes[val] += 1
            else:
                sizes[val] = 1
        return sorted([val for val in sizes.values()], reverse=True)



class Location:
    position = None
    neighbors = None

class Field:
    field = None
    graph = None

    def __init__(self, lines):
        height = len(lines)
        width = len(lines[0])
        near = [(-1,0),(1,0), (0,1),(0,-1) ]

        self.field = []
        self.field.append([10]*(width+2))
        for ln in lines:
            self.field.append([10] + list(map(int, list(ln))) + [10])
        self.field.append([10]*(width+2))

        self.graph = {}
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                tmp_pos = (i, j)
                tmp_neigh = []
                tmp_height = self.field[i][j]
                if tmp_height < 9:
                    for (x, y) in near:
                        if (0 <= i+x < len(self.field)) and (0 <= j+y < len(self.field[i])):
                            if self.field[i+x][j+y] <9:
                                tmp_neigh.append((i+x, j+y))
                    self.graph[(i,j)] = (tmp_height, tmp_neigh)


    def return_min_points(self):
        near = [(-1,0),(1,0), (0,1),(0,-1) ]
        lowers = []
        for i in range(1, len(self.field)-1):
            for j in range(1, len(self.field[i])-1):
                lower = True
                for (x,y) in near:
                    if self.field[i+x][j+y] <= self.field[i][j]:
                        lower = False
                if lower:
                    lowers.append(((i-1,j-1), self.field[i][j]))
        return lowers

    def return_min_points_neighbors(self):
        lowers = []

        for location in self.graph:
            (h, nb) = self.graph[location]
            lower = True
            for neighbor in nb:
                (npos, _) = self.graph[neighbor]
                if npos <= h:
                    lower = False
            if lower:
                lowers.append((location, h))
        return lowers

    def connected_fields(self):
        uf = UF(self.graph)

        uf.solve()
        return  uf.basin_sizes()