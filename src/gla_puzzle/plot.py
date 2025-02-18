import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

mpl.use("agg")

from gla_puzzle import Grid

num = 0


def plot_grid(grid: Grid) -> None:
    """Plot the grid."""
    global num  # noqa: PLW0603
    plt.figure(dpi=100, figsize=(6, 6))
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    pieces_names = {value for value in grid.map.values() if value is not None}
    cmap = plt.get_cmap("tab20", len(pieces_names))
    colors = {name: cmap(i) for i, name in enumerate(sorted(pieces_names))}
    colors[None] = "white"

    for triangle, value in grid.map.items():
        polygon = Polygon(
            [(point.x, point.y) for point in (triangle.a, triangle.b, triangle.c)],
            edgecolor="black",
            facecolor=colors[value],
        )
        plt.gca().add_patch(polygon)

    plt.savefig(f"imgs/grid{num:05d}.jpg")
    num += 1
    plt.close()
