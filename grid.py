import numpy as np

def create_grid(nx, ny):
    return {
        "u": np.zeros((nx+1, ny)),     # x방향 속도 (u)
        "v": np.zeros((nx, ny+1)),     # y방향 속도 (v)
        "p": np.zeros((nx, ny)),       # 압력 (p)
        "div": np.zeros((nx, ny)),     # 발산 (divergence)
        "nx": nx,
        "ny": ny
    }
