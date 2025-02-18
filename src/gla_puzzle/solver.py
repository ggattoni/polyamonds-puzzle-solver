from tqdm import tqdm

from gla_puzzle.grid import Grid
from gla_puzzle.piece import Piece
from gla_puzzle.plot import plot_grid


def solve(
    grid: Grid, remaining_pieces: list[Piece], *, plot: bool = False, tqdm_position: int = 0, optimize: bool = False
) -> tuple[Grid, bool]:
    """Solve the puzzle."""
    if plot:
        plot_grid(grid)
    if not remaining_pieces:
        return grid, True

    piece = remaining_pieces[0]
    other_pieces = remaining_pieces[1:]

    for piece_variation in tqdm(
        piece.get_all_variations(optimize=optimize), position=tqdm_position, desc=piece.name, leave=tqdm_position == 0
    ):
        for point in tqdm(
            grid.available_points(piece_variation), position=tqdm_position + 1, desc="Points", leave=False
        ):
            new_grid = grid.place_piece(piece_variation, point)
            solution, solved = solve(
                new_grid, other_pieces, plot=plot, tqdm_position=tqdm_position + 2, optimize=optimize
            )
            if solved:
                return solution, True

    return grid, False


def solve_all(
    grid: Grid, remaining_pieces: list[Piece], *, plot: bool = False, tqdm_position: int = 0, optimize: bool = False
) -> tuple[Grid, bool]:
    """Solve the puzzle."""
    if plot:
        plot_grid(grid)

    if not remaining_pieces:
        return grid, True

    piece = remaining_pieces[0]
    other_pieces = remaining_pieces[1:]

    for piece_variation in tqdm(
        piece.get_all_variations(optimize=optimize), position=tqdm_position, desc=piece.name, leave=tqdm_position == 0
    ):
        for point in tqdm(
            grid.available_points(piece_variation), position=tqdm_position + 1, desc="Points", leave=False
        ):
            new_grid = grid.place_piece(piece_variation, point)
            solution, solved = solve_all(
                new_grid, other_pieces, plot=plot, tqdm_position=tqdm_position + 2, optimize=optimize
            )
            if solved:
                plot_grid(solution)

    return grid, False


if __name__ == "__main__":
    # from gla_puzzle.puzzles.xtechai import GRID, PIECES
    from gla_puzzle.puzzles.luciano import GRID, PIECES

    pieces = sorted(PIECES, key=lambda piece: len(piece.triangles), reverse=True)

    # solution, _ = solve(GRID, pieces)
    # plot_grid(solution)

    solve_all(GRID, pieces, optimize=True, plot=False)
