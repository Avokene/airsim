import numpy as np

def bilinear_sample(field, x, y):
    """
    x, y는 실수형 인덱스 (격자 좌표계 기준)
    2D bilinear interpolation
    """
    x0 = int(np.floor(x))
    x1 = x0 + 1
    y0 = int(np.floor(y))
    y1 = y0 + 1

    x0 = np.clip(x0, 0, field.shape[0] - 1)
    x1 = np.clip(x1, 0, field.shape[0] - 1)
    y0 = np.clip(y0, 0, field.shape[1] - 1)
    y1 = np.clip(y1, 0, field.shape[1] - 1)

    fx = x - x0
    fy = y - y0

    val = (
        field[x0, y0] * (1 - fx) * (1 - fy) +
        field[x1, y0] * fx * (1 - fy) +
        field[x0, y1] * (1 - fx) * fy +
        field[x1, y1] * fx * fy
    )

    return val
