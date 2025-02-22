from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

mpl.use("agg")

from polyamonds_puzzle_solver import Grid

num = 0


def plot_grid(grid: Grid, folder: Path | None = None) -> None:
    """Plot the grid."""
    global num  # noqa: PLW0603
    plt.figure(dpi=300, figsize=(6, 6))

    pieces_names = {value for value in grid.map.values() if value is not None}
    cmap = plt.get_cmap("tab20", len(pieces_names))
    colors = {name: cmap(i) for i, name in enumerate(sorted(pieces_names))}
    colors[None] = "white"

    min_lim = 1e6
    max_lim = -1e6
    for triangle in grid.map:
        for point in (triangle.a, triangle.b, triangle.c):
            x, y = point.coordinates
            min_lim = min(min_lim, x, y)
            max_lim = max(max_lim, x, y)
    plt.xlim(min_lim, max_lim)
    plt.ylim(min_lim, max_lim)

    for triangle, value in grid.map.items():
        polygon = Polygon(
            # [(point.x * X_UNIT, point.y * Y_UNIT) for point in (triangle.a, triangle.b, triangle.c)],
            [point.coordinates for point in (triangle.a, triangle.b, triangle.c)],
            edgecolor="black",
            facecolor=colors[value],
        )
        plt.gca().add_patch(polygon)

    if folder is None:
        folder = Path("solutions")
    folder.mkdir(exist_ok=True)

    plt.axis("off")
    plt.tight_layout()
    plt.savefig(folder / f"solution_{num:05d}.png", transparent=True)
    num += 1
    plt.close()
