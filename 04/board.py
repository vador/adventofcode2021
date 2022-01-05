import logging

class Board:
    numbers = None
    columns = None
    lines = None
    win = None

    def __init__(self, strBoard):
        self.numbers  = {}
        for (i, line) in enumerate(strBoard):
            for (j,number) in enumerate(line.split()):
                self.numbers[int(number)] = (i,j)
        self.win = len(strBoard)
        self.columns = [0] * self.win
        self.lines = [0] * self.win

    def __repr__(self):
        return str(self.numbers)

    def drawNumber(self, number):
        if number in self.numbers:
            (i,j) = self.numbers[number]
            self.lines[i] += 1
            self.columns[j] += 1
            self.numbers.pop(number)
            if (self.lines[i] == self.win) or (self.columns[j] == self.win):
                return sum(self.numbers.keys())
        return False






