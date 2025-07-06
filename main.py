def init():
    grid = []
    for y in range(4):
        grid.append([])
        for x in range(4):
            grid[y].append(x)

    # May want to move this into a self standing function so the data types don't not get messed up.
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    return grid


    # We need to asses how this grid is made, so we can manipulate it with the moving functions
init()
print(grid.type)
