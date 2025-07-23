from utils import bilinear_sample

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
    """
    외부에서 유체에 작용하는 힘을 적용합니다.
    예: 입구 유속, 중력 등

    여기서는 단순히 왼쪽 벽에서 유입 유속을 고정합니다.
    """
    u = grid["u"]
    nx, ny = grid["nx"], grid["ny"]

    # 왼쪽 벽에서 u 속도를 1.0으로 설정 (유입 조건)
    u[0, :] = 1.0



import numpy as np

def advect(grid, dt):
    """
    Semi-Lagrangian 방식의 Advection
    속도장에 따라 u, v 벡터가 이동함
    """
    u = grid["u"]
    v = grid["v"]
    nx, ny = grid["nx"], grid["ny"]
    dx, dy = grid["dx"], grid["dy"]

    # 새로운 속도를 저장할 임시 배열
    new_u = np.zeros_like(u)
    new_v = np.zeros_like(v)

    # u 속도 이동
    for i in range(1, nx):
        for j in range(ny):
            x = i * dx
            y = (j + 0.5) * dy

            # 현재 위치의 속도
            vel_x = u[i, j]
            vel_y = 0.25 * (v[i - 1, j] + v[i, j] + v[i - 1, j + 1] + v[i, j + 1])

            # 이전 위치를 따라 역추적
            prev_x = x - dt * vel_x
            prev_y = y - dt * vel_y

            new_u[i, j] = bilinear_sample(u, prev_x / dx, prev_y / dy)

    # v 속도 이동
    for i in range(nx):
        for j in range(1, ny):
            x = (i + 0.5) * dx
            y = j * dy

            vel_x = 0.25 * (u[i, j - 1] + u[i + 1, j - 1] + u[i, j] + u[i + 1, j])
            vel_y = v[i, j]

            prev_x = x - dt * vel_x
            prev_y = y - dt * vel_y

            new_v[i, j] = bilinear_sample(v, prev_x / dx, prev_y / dy)

    grid["u"] = new_u
    grid["v"] = new_v


def solve_pressure(grid, dt, iterations=50):
    """
    속도 발산을 제거하기 위해 압력 보정 수행
    Poisson 방정식을 Jacobi 방식으로 풀이

    ∇²p = div(u) / dt
    """
    u, v = grid["u"], grid["v"]
    p = grid["p"]
    div = grid["div"]

    nx, ny = grid["nx"], grid["ny"]
    dx, dy = grid["dx"], grid["dy"]

    # 발산 계산
    for i in range(nx):
        for j in range(ny):
            div[i, j] = -0.5 * (
                (u[i + 1, j] - u[i, j]) / dx +
                (v[i, j + 1] - v[i, j]) / dy
            )

    # 압력 초기화
    p.fill(0.0)
    dx2, dy2 = dx * dx, dy * dy
    denom = 2.0 * (dx2 + dy2)

    for _ in range(iterations):
        p_new = np.copy(p)

        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                p_new[i, j] = (
                    (p[i + 1, j] + p[i - 1, j]) * dy2 +
                    (p[i, j + 1] + p[i, j - 1]) * dx2 -
                    div[i, j] * dx2 * dy2
                ) / denom

        p[:] = p_new

    grid["p"] = p


def project(grid, dt):
    """
    압력을 이용해 속도장을 무발산 상태로 보정
    """
    u, v = grid["u"], grid["v"]
    p = grid["p"]
    nx, ny = grid["nx"], grid["ny"]
    dx, dy = grid["dx"], grid["dy"]

    for i in range(1, nx):
        for j in range(ny):
            u[i, j] -= dt * (p[i, j] - p[i - 1, j]) / dx

    for i in range(nx):
        for j in range(1, ny):
            v[i, j] -= dt * (p[i, j] - p[i, j - 1]) / dy


def apply_boundary_conditions(grid):
    """
    경계 조건을 적용합니다.
    벽에서는 속도가 0이 되도록, 유입/출구에서는 적절히 복사합니다.
    """
    u = grid["u"]
    v = grid["v"]
    nx, ny = grid["nx"], grid["ny"]

    # u 벽 경계 처리
    u[0, :] = 1.0           # 좌측 유입 (Dirichlet)
    u[-1, :] = u[-2, :]     # 우측 출구 (Neumann)
    u[:, 0] = -u[:, 1]      # 하단 벽
    u[:, -1] = -u[:, -2]    # 상단 벽

    # v 벽 경계 처리
    v[0, :] = -v[1, :]      # 좌측 벽
    v[-1, :] = -v[-2, :]    # 우측 벽
    v[:, 0] = 0.0           # 하단 벽
    v[:, -1] = 0.0          # 상단 벽

