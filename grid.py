import numpy as np

def create_grid(nx: int, ny: int, dx=1.0, dy=1.0):
    """
    시뮬레이션 격자 및 변수 초기화

    Args:
        nx (int): x 방향 격자 수
        ny (int): y 방향 격자 수
        dx (float): x 방향 셀 간격
        dy (float): y 방향 셀 간격

    Returns:
        dict: 유체 시뮬레이션 변수 포함
    """
    grid = {
        # 속도 벡터 (MAC 방식)
        "u": np.zeros((nx + 1, ny)),    # u: x방향 속도 (cell 경계에 위치)
        "v": np.zeros((nx, ny + 1)),    # v: y방향 속도 (cell 경계에 위치)

        # 압력 및 보조 변수
        "p": np.zeros((nx, ny)),        # 압력
        "div": np.zeros((nx, ny)),      # 발산 (divergence)

        # 격자 정보
        "nx": nx,
        "ny": ny,
        "dx": dx,
        "dy": dy
    }

    return grid