from pathlib import Path

from tqdm import tqdm

from gla_puzzle.grid import Grid
from gla_puzzle.piece import Piece
from gla_puzzle.plot import plot_grid


def _find_first_solution(
    grid: Grid, remaining_pieces: list[Piece], *, plot: bool = False, tqdm_position: int = 0
) -> tuple[Grid, bool]:
    """Solve the puzzle."""
    if plot:
        plot_grid(grid)
    if not remaining_pieces:
        return grid, True

    piece = remaining_pieces[0]
    other_pieces = remaining_pieces[1:]

    for piece_variation in tqdm(
        piece.get_all_variations(), position=tqdm_position, desc=piece.name, leave=tqdm_position == 0
    ):
        for point in tqdm(
            grid.available_points(piece_variation), position=tqdm_position + 1, desc="Points", leave=False
        ):
            new_grid = grid.place_piece(piece_variation, point)
            solution, solved = _find_first_solution(new_grid, other_pieces, plot=plot, tqdm_position=tqdm_position + 2)
            if solved:
                return solution, True

    return grid, False


def _find_all_solutions(
    grid: Grid, remaining_pieces: list[Piece], folder: Path | None = None, *, plot: bool = False, tqdm_position: int = 0
) -> tuple[Grid, bool]:
    """Solve the puzzle."""
    if plot:
        plot_grid(grid, folder=folder / "tmp")

    if not remaining_pieces:
        return grid, True

    piece = remaining_pieces[0]
    other_pieces = remaining_pieces[1:]

    for piece_variation in tqdm(
        piece.get_all_variations(), position=tqdm_position, desc=piece.name, leave=tqdm_position == 0
    ):
        for point in tqdm(
            grid.available_points(piece_variation), position=tqdm_position + 1, desc="Points", leave=False
        ):
            new_grid = grid.place_piece(piece_variation, point)
            solution, solved = _find_all_solutions(new_grid, other_pieces, plot=plot, tqdm_position=tqdm_position + 2)
            if solved:
                plot_grid(solution, folder=folder)

    return grid, False


def solve(grid: Grid, pieces: list[Piece], folder: Path | None = None, *, verbose: bool = False) -> None:  # noqa: ARG001
    """Solve the puzzle."""
    sorted_pieces = sorted(pieces, key=lambda piece: len(piece.triangles), reverse=True)
    _find_all_solutions(grid, sorted_pieces, folder=folder, plot=False)
