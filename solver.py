def run_simulation(grid, dt):
    # 1. 외력 적용 (ex. 유입 속도)
    apply_forces(grid)

    # 2. 속도 예측 (모멘텀 방정식)
    advect(grid)

    # 3. 압력 계산 (Poisson 방정식)
    solve_pressure(grid)

    # 4. 속도 보정 (divergence-free)
    project(grid)

    # 5. 경계 조건 적용
    apply_boundary_conditions(grid)
