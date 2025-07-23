from solver import run_simulation
from grid import create_grid
from visualize import visualize

# 격자 크기 및 시간 설정
nx, ny = 64, 64
dt = 0.01
steps = 500

# 격자 생성
grid = create_grid(nx, ny)

# 시뮬레이션 실행
for step in range(steps):
    run_simulation(grid, dt)
    visualize(grid, step)
