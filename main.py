# from solver import run_simulation
from grid import create_grid
# from visualize import visualize

# 격자 크기 및 시간 설정
nx, ny = 64, 64
dt = 0.01
steps = 500

# 격자 생성
grid = create_grid(nx, ny)

# 시뮬레이션 실행
for step in range(steps):
    print("u shape:", grid["u"].shape)
    print("v shape:", grid["v"].shape)
    print("p shape:", grid["p"].shape)
    # run_simulation(grid, dt)
    # visualize(grid, step)
