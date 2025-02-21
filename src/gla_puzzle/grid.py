from __future__ import annotations

from functools import cache, cached_property
from typing import TYPE_CHECKING

from frozendict import frozendict

from gla_puzzle.point import Point
from gla_puzzle.triangle import Triangle

if TYPE_CHECKING:
    from collections.abc import Iterable

    from gla_puzzle.piece import Piece


@cache
def _empty_triangles(grid: Grid) -> list[Triangle]:
    """Return a list of empty triangles."""
    return [triangle for triangle, value in grid.map.items() if value is None]


@cache
def _available_points(grid: Grid, piece: Piece) -> Iterable[Point]:
    """Return a set of available points for a piece."""
    return (point for point in grid.points if (piece + point) in grid)


@cache
def _contains(grid: Grid, piece: Piece) -> bool:
    """Check if a piece is contained in the grid."""
    return all(triangle in grid.triangles and grid.map[triangle] is None for triangle in piece.triangles)


@cache
def _place_piece(grid: Grid, piece: Piece, point: Point) -> Grid:
    """Place a piece in the grid."""
    new_grid = Grid(grid.triangles)
    new_grid.map = grid.map
    new_grid.integer_mapping = grid.integer_mapping
    for triangle in piece.triangles:
        new_grid.map = new_grid.map.set(triangle + point, piece.name)
    return new_grid


class Grid:
    """Grid class."""

    def __init__(self, triangles: set[Triangle]) -> None:
        """Initialize the grid."""
        self.triangles = triangles

        self.map: frozendict[Triangle, str | None] = frozendict({triangle: None for triangle in self.triangles})
        self.integer_mapping: frozendict[Triangle, int] = frozendict(
            {triangle: i for i, triangle in enumerate(self.triangles)}
        )

    @cached_property
    def points(self) -> set[Point]:
        """Return a set of points in the grid."""
        return {point for triangle in self.triangles for point in (triangle.a, triangle.b, triangle.c)}

    def empty_triangles(self) -> list[Triangle]:
        """Return a list of empty triangles."""
        return _empty_triangles(self)

    def available_points(self, piece: Piece) -> set[Point]:
        """Return a set of available points for a piece."""
        return _available_points(self, piece)

    def __contains__(self, piece: Piece) -> bool:
        """Check if a piece is contained in the grid."""
        return _contains(self, piece)

    def place_piece(self, piece: Piece, point: Point) -> Grid:
        """Place a piece in the grid."""
        return _place_piece(self, piece, point)

    def __eq__(self, value: Grid) -> bool:
        """Check if two grids are equal."""
        return self.map == value.map

    def __hash__(self) -> int:
        """Return the hash of the grid."""
        return hash(self.map)


def create_triangle_line(num_triangles: int, leftmost_point: Point, *, up: bool) -> list[Triangle]:
    """Create a line of triangles."""
    triangles = []
    for _ in range(num_triangles):
        if up:
            a = leftmost_point + Point(0, 0)
            b = leftmost_point + Point(1, 1)
            c = leftmost_point + Point(2, 0)
            leftmost_point = b
        else:
            a = leftmost_point + Point(0, 0)
            b = leftmost_point + Point(2, 0)
            c = leftmost_point + Point(1, -1)
            leftmost_point = c
        triangles.append(Triangle(a, b, c))
        up = not up
    return triangles


# TODO: Implement create grid function given only list of number of triangles
