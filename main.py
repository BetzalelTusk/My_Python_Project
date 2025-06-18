import tkinter as tk


def init():
    grid = []
    for y in range(4):
        grid.append([])
        for x in range(4):
            grid[y].append(x)
    for row in grid:
        print(" ".join(str(cell) for cell in row))


init()
