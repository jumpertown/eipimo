"""Image and graph util functions."""
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


BORDER = 0.3


def draw_path(path, colour='blue'):
    """Draw a path from a list of coordinates."""
    codes = [Path.LINETO] * len(path)
    codes[0] = Path.MOVETO
    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(
        Path(path, codes),
        facecolor=colour,
        lw=2
    )
    x_min, y_min = path[0]
    x_max, y_max = path[0]

    for x, y in path:
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y

    ax.add_patch(patch)
    ax.set_xlim(x_min - BORDER, x_max + BORDER)
    ax.set_ylim(y_min - BORDER, y_max + BORDER)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
