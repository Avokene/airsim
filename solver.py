def run_simulation(grid, dt):
    """
    한 스텝 동안 유체 시뮬레이션 실행

    Args:
        grid (dict): 시뮬레이션 격자 및 변수
        dt (float): 시간 간격
    """
    # 1. 외력 적용 (예: 중력, 유입 속도 등)
    apply_forces(grid, dt)

    # 2. 속도 이동 (Advection)
    advect(grid, dt)

    # 3. 압력 보정 (Poisson 방정식)
    solve_pressure(grid, dt)

    # 4. 속도 보정 (Divergence 제거)
    project(grid, dt)

    # 5. 경계 조건 적용
    apply_boundary_conditions(grid)


def apply_forces(grid, dt):
    # 예: 유입 속도 등 외력을 추가하는 부분
    pass


def advect(grid, dt):
    # 반송(Advection): 유체가 자기 자신을 운반
    pass


def solve_pressure(grid, dt):
    # Poisson 방정식으로 압력 계산
    pass


def project(grid, dt):
    # 압력 보정 후, 속도 필드를 무발산(divergence-free)으로 수정
    pass


def apply_boundary_conditions(grid):
    # 벽, 입출구 등 경계 조건 적용
    pass
