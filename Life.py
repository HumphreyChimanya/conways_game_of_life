from collections import defaultdict
import time
import os

def get_neighbors(cell):
    r, c = cell
    return [
        (r + dr, c + dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if not (dr == 0 and dc == 0)
    ]

def timestep(live_cells):
    neighbor_counts = defaultdict(int)

    for cell in live_cells:
        for neighbor in get_neighbors(cell):
            neighbor_counts[neighbor] += 1

    new_live_cells = set()
    for cell, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live_cells.add(cell)

    return new_live_cells

def print_grid(live_cells, bounds):
    os.system('clear')  # use 'cls' if on Windows
    r_min, r_max, c_min, c_max = bounds
    for r in range(r_min, r_max):
        for c in range(c_min, c_max):
            print("⬜" if (r, c) in live_cells else "  ", end='')
        print()
    print()

def simulate_infinite(initial_cells, steps, bounds):
    live_cells = set(initial_cells)
    for _ in range(steps):
        print_grid(live_cells, bounds)
        time.sleep(0.2)
        live_cells = timestep(live_cells)

# Example: Glider
glider = [
    (1, 2),
    (2, 3),
    (3, 1), (3, 2), (3, 3)
]

# Simulate
simulate_infinite(glider, steps=100, bounds=(0, 20, 0, 40))

