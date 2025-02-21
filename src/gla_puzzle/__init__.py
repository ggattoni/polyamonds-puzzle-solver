"""The gla_puzzle package provides classes for creating and solving puzzles created by Glauco."""

import importlib
from pathlib import Path

import click

from .grid import Grid, create_triangle_line
from .piece import Piece
from .point import X_UNIT, Y_UNIT, Point
from .triangle import Triangle

__all__ = ["X_UNIT", "Y_UNIT", "Grid", "Piece", "Point", "Triangle", "create_triangle_line"]


@click.group()
@click.version_option()
def cli() -> None:
    """Solver for tangram-like polyamonds puzzles."""


@cli.command(name="solve")
@click.argument("puzzle")
@click.option(
    "-s",
    "--solver",
    type=click.Choice(["brute-force", "cpsat"]),
    default="cpsat",
    help="Which solver to use",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Log additional information",
)
def solve(puzzle: str, solver: str, *, verbose: bool = False) -> None:
    """Solve the puzzle with the desired solver."""
    try:
        puzzle_module = importlib.import_module(f"gla_puzzle.puzzles.{puzzle}")
    except ModuleNotFoundError:
        click.echo(f"{puzzle} not found.")
        return

    grid: Grid = puzzle_module.GRID
    pieces: list[Piece] = puzzle_module.PIECES

    if solver == "brute-force":
        from .solvers.brute_force import solve
    elif solver == "cpsat":
        from .solvers.cpsat import solve

    solve(grid, pieces, folder=Path("solutions") / puzzle, verbose=verbose)
