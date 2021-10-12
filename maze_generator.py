import random
import math


class Generator(object):
    def __init__(self, startx, starty, sizex=11, sizey=11):
        self.Grid = [[0 for i in range(sizex)] for j in range(sizey)]
        self.Grid[starty][startx] = 1
        self.Frontier = []
        self.sizex = sizex
        self.sizey = sizey
        # print(startx, starty)
        self.CalculateFrontier(startx, starty)
        # print(self.Frontier)
        # print(self.Frontier)
        while (len(self.Frontier) > 0):
            self.Expand()
        # self.AddLoops(math.floor(math.sqrt(sizex*sizey)-1/2))
        # print(self.Grid)
        # self.PrintGrid()

    def PrintGrid(self):
        for row in self.Grid:
            for cell in row:
                if (cell == 0):
                    print(" ", end=" ")
                else:
                    print("\u25A0", end=" ")
            print("\n", end="")

    def CalculateFrontier(self, x, y):
        if (x >= 0 and x <= self.sizex - 1 and y >= 0 and y <= self.sizey - 1):
            if (x - 2 >= 0 and x - 2 <= self.sizex - 1 and self.Grid[y][x - 2] != 1):
                if (not [x - 2, y] in self.Frontier):
                    self.Frontier.append([x - 2, y])

            if (x + 2 >= 0 and x + 2 <= self.sizex - 1 and self.Grid[y][x + 2] != 1):
                if (not [x + 2, y] in self.Frontier):
                    self.Frontier.append([x + 2, y])

            if (y - 2 >= 0 and y - 2 <= self.sizey - 1 and self.Grid[y - 2][x] != 1):
                if (not [x, y - 2] in self.Frontier):
                    self.Frontier.append([x, y - 2])

            if (y + 2 >= 0 and y + 2 <= self.sizey - 1 and self.Grid[y + 2][x] != 1):
                if (not [x, y + 2] in self.Frontier):
                    self.Frontier.append([x, y + 2])

    def GetNeighbors(self, x, y):
        Neighbors = []
        if (x >= 0 and x <= self.sizex - 1 and y >= 0 and y <= self.sizey - 1):
            if (x - 2 >= 0):
                if (self.Grid[y][x - 2] == 1):
                    Neighbors.append([x - 2, y])

            if (x + 2 <= self.sizex - 1):
                if (self.Grid[y][x + 2] == 1):
                    Neighbors.append([x + 2, y])

            if (y - 2 >= 0):
                if (self.Grid[y - 2][x] == 1):
                    Neighbors.append([x, y - 2])

            if (y + 2 <= self.sizey - 1):
                if (self.Grid[y + 2][x] == 1):
                    Neighbors.append([x, y + 2])
        return Neighbors

    def Mid(self, p1, p2):
        x = y = 0
        # X is equal
        if (p1[0] == p2[0]):
            x = p1[0]
            # Calc y
            if (p1[1] > p2[1]):
                y = p2[1] + 1
            else:
                y = p1[1] + 1

        # Y is equal
        elif (p1[1] == p2[1]):
            y = p1[1]
            # Calc x
            if (p1[0] > p2[0]):
                x = p2[0] + 1
            else:
                x = p1[0] + 1

        return [x, y]

    def Expand(self):
        # Choose a random frontier vertex
        FrontierIndex = random.randint(0, len(self.Frontier) - 1)
        FE = self.Frontier[FrontierIndex]
        Neighbors = self.GetNeighbors(FE[0], FE[1])
        NeighborIndex = random.randint(0, len(Neighbors) - 1)

        # Calculate the midpoint between the frontier vertex and existing pathway
        Mid = self.Mid(FE, Neighbors[NeighborIndex])
        x = Mid[0]
        y = Mid[1]

        # Set the frontier vertex and midpoint to a pathway
        self.Grid[FE[1]][FE[0]] = 1
        self.Grid[y][x] = 1

        # Remove the frontier vertex from the frontier list
        self.Frontier.remove(FE)

        # Calculate the new frontier vertices
        self.CalculateFrontier(FE[0], FE[1])

    def AddLoops(self, NumLoops):
        for i in range(NumLoops):
            # Get a random vertex and one of it's neighbors
            p1 = [round(random.randint(0, self.sizex - 1) / 2) * 2, round(random.randint(0, self.sizey - 1) / 2) * 2]
            p2 = random.choice(self.GetNeighbors(p1[0], p1[1]))

            # Get new vertices if the current ones are already linked
            while (self.Grid[self.Mid(p1, p2)[1]][self.Mid(p1, p2)[0]] == 1):
                p1 = [round(random.randint(0, self.sizex - 1) / 2) * 2,
                      round(random.randint(0, self.sizey - 1) / 2) * 2]
                p2 = random.choice(self.GetNeighbors(p1[0], p1[1]))
            self.Grid[self.Mid(p1, p2)[1]][self.Mid(p1, p2)[0]] = 1


if __name__ == "__main__":
    GridSizex = 32
    GridSizey = 32

    x = math.floor(random.randint(0, GridSizex) / 2) * 2
    y = math.floor(random.randint(0, GridSizey) / 2) * 2

    Generator(x, y, GridSizex, GridSizey)
