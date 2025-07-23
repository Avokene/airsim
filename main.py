from grid import create_grid
from solver import run_simulation
from visualize import visualize

nx, ny = 64, 64
grid = create_grid(nx, ny)
dt = 0.01
steps = 300

for step in range(steps):
    run_simulation(grid, dt)
    if step % 5 == 0:  # 시각화 빈도 조절 가능
        visualize(grid, step)
