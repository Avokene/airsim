import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
plt.ion()  # 인터랙티브 모드 활성화

colorbar = None  # colorbar 중복 방지용 핸들

def visualize(grid, step):
    global colorbar

    u = grid["u"]
    v = grid["v"]
    p = grid["p"]
    nx, ny = grid["nx"], grid["ny"]
    dx, dy = grid["dx"], grid["dy"]

    # 속도 중심 위치 계산
    u_center = 0.5 * (u[:-1, :] + u[1:, :])
    v_center = 0.5 * (v[:, :-1] + v[:, 1:])
    speed = np.sqrt(u_center**2 + v_center**2)

    x = np.linspace(0.5 * dx, (nx - 0.5) * dx, nx)
    y = np.linspace(0.5 * dy, (ny - 0.5) * dy, ny)
    X, Y = np.meshgrid(x, y, indexing='ij')

    # --- 압력 맵 ---
    ax1.clear()
    ax1.set_title(f"Pressure Field (Step {step})")
    im = ax1.imshow(p.T, origin="lower", cmap="coolwarm", extent=[0, nx*dx, 0, ny*dy])
    if colorbar is None:
        colorbar = fig.colorbar(im, ax=ax1)

    # --- 속도 벡터 ---
    ax2.clear()
    ax2.set_title("Velocity Field")
    ax2.set_xlim(0, nx * dx)
    ax2.set_ylim(0, ny * dy)
    ax2.quiver(
        X, Y,
        u_center, v_center,
        speed,                  # 벡터 컬러 (optional)
        scale=None,             # 자동 스케일
        angles="xy",
        scale_units="xy",
        cmap="viridis",
        width=0.003,
        pivot="mid"
    )

    plt.pause(0.001)
