#Two-dimentional lists are like grids

number_grid = [
    [1, 2, 3],
    [4, 235, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)