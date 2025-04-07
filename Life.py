import os
import time
import numpy as np


def make_grid(rows, cols, live_cells):
    grid = np.zeros((rows + 2, cols + 2), dtype=np.int8)
    for r, c in live_cells:
        grid[r + 1, c + 1] = 1  # offset for ghost cells
    return grid


def print_grid(grid, interactive=False):
    if interactive:
        time.sleep(0.05)
        os.system('cls' if os.name == 'nt' else 'clear')
    rows, cols = grid.shape
    print('-' * (cols + 1))
    for i in range(1, rows - 1):
        print('|', end='')
        for j in range(1, cols - 1):
            print('■' if grid[i, j] else '  ', end='')  # white heart for alive cells
        print('|')
    print('-' * (cols + 1))
    print()


def timestep(current_grid, next_grid):
    for i in range(1, current_grid.shape[0] - 1):
        for j in range(1, current_grid.shape[1] - 1):
            neighbors = np.sum(current_grid[i - 1:i + 2, j - 1:j + 2]) - current_grid[i, j]
            if current_grid[i, j] == 1:
                next_grid[i, j] = 1 if neighbors in (2, 3) else 0
            else:
                next_grid[i, j] = 1 if neighbors == 3 else 0


def simulate(rows, cols, steps, live_cells, interactive=False):
    current_grid = make_grid(rows, cols, live_cells)
    next_grid = make_grid(rows, cols, [])

    for _ in range(steps):
        print_grid(current_grid, interactive)
        timestep(current_grid, next_grid)
        current_grid, next_grid = next_grid, current_grid


if __name__ == "__main__":
    # Two gliders: one top-left, one in the middle
    glider = [
        (1, 2), (2, 3), (3, 1), (3, 2), (3, 3),
        (10, 10), (10, 11), (11, 10), (11, 12), (12, 11),]

    simulate(rows=20, cols=40, steps=100, live_cells=glider, interactive=True)
