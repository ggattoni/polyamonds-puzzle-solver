from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from typing import TYPE_CHECKING, Literal

import sympy as sp

from gla_puzzle.point import Point

if TYPE_CHECKING:
    from gla_puzzle.triangle import Triangle


@cache
def _add(piece: Piece, point: Point) -> Point:
    """Translate the piece by a point."""
    return Piece(name=piece.name, triangles={triangle + point for triangle in piece.triangles})


@cache
def _sub(piece: Piece, point: Point) -> Point:
    """Translate the piece by a point."""
    return Piece(name=piece.name, triangles={triangle - point for triangle in piece.triangles})


@cache
def _neg(piece: Piece) -> Piece:
    """Reflect the piece across the x-axis."""
    return Piece(name=piece.name, triangles={-triangle for triangle in piece.triangles})


@cache
def _rotate(piece: Piece, angle: sp.Expr) -> Piece:
    """Rotate the piece wrt to the origin."""
    return Piece(name=piece.name, triangles={triangle @ angle for triangle in piece.triangles})


@cache
def _reflect(piece: Piece, axis: Literal["x", "y"]) -> Piece:
    """Reflect the piece across the specified axis."""
    return Piece(
        name=piece.name,
        triangles={triangle.reflect(axis=axis) for triangle in piece.triangles},
    )


# @cache
# def _is_central_symmetric(piece: Piece) -> bool:
#     """Check if the piece is central symmetric."""
#     return piece == -(piece @ sp.pi)


@cache
def _is_central_translation_symmetric(piece: Piece) -> bool:
    """Check if the piece is central translation symmetric."""
    translated_piece = piece @ sp.pi
    y_shift = max(max(triangle.a.y, triangle.b.y, triangle.c.y) for triangle in piece.triangles) - max(
        max(triangle.a.y, triangle.b.y, triangle.c.y) for triangle in (piece @ sp.pi).triangles
    )
    x_shift = max(max(triangle.a.x, triangle.b.x, triangle.c.x) for triangle in piece.triangles) - max(
        max(triangle.a.x, triangle.b.x, triangle.c.x) for triangle in (piece @ sp.pi).triangles
    )
    translated_piece = translated_piece + Point(x_shift, y_shift)
    return piece == translated_piece


@cache
def _is_reflection_same(piece: Piece) -> bool:
    """Check if the piece is the same after reflection."""
    reflected_piece_x = piece.reflect(axis="x")
    y_shift = max(max(triangle.a.y, triangle.b.y, triangle.c.y) for triangle in piece.triangles) - max(
        max(triangle.a.y, triangle.b.y, triangle.c.y) for triangle in reflected_piece_x.triangles
    )
    x_shift = max(max(triangle.a.x, triangle.b.x, triangle.c.x) for triangle in piece.triangles) - max(
        max(triangle.a.x, triangle.b.x, triangle.c.x) for triangle in reflected_piece_x.triangles
    )
    reflected_piece_x = reflected_piece_x + Point(x_shift, y_shift)

    reflected_piece_y = piece.reflect(axis="y")
    y_shift = max(max(triangle.a.y, triangle.b.y, triangle.c.y) for triangle in piece.triangles) - max(
        max(triangle.a.y, triangle.b.y, triangle.c.y) for triangle in reflected_piece_y.triangles
    )
    x_shift = max(max(triangle.a.x, triangle.b.x, triangle.c.x) for triangle in piece.triangles) - max(
        max(triangle.a.x, triangle.b.x, triangle.c.x) for triangle in reflected_piece_y.triangles
    )
    reflected_piece_y = reflected_piece_y + Point(x_shift, y_shift)

    return piece in (reflected_piece_x, reflected_piece_y)


@cache
def _get_all_variations(piece: Piece, *, optimize: bool = False) -> list[Piece]:
    """Return all possible variations of the piece."""
    transforms = []
    step = 1
    reflect = True
    if optimize and any(_is_central_translation_symmetric(piece @ (k * sp.pi / 3)) for k in range(6)):
        step = 2
    if optimize and any(_is_reflection_same(piece @ (k * sp.pi / 3)) for k in range(6)):
        reflect = False
    for k in range(0, 6, step):
        rotated_piece = piece @ (k * sp.pi / 3)
        transforms.append(rotated_piece)
        if reflect:
            transforms.append(rotated_piece.reflect(axis="x"))
            # transforms.append(piece.reflect(axis="y"))
    return transforms


@dataclass
class Piece:
    """Piece class."""

    name: str
    triangles: set[Triangle]

    def __eq__(self, other: Piece) -> bool:
        """Check if two pieces are equal."""
        return self.triangles == other.triangles

    def __hash__(self) -> int:
        """Return the hash of the piece."""
        return hash(frozenset(self.triangles))

    def __add__(self, point: Point) -> Piece:
        """Translate the piece by a point."""
        return _add(self, point)

    def __sub__(self, point: Point) -> Piece:
        """Translate the piece by a point."""
        return _sub(self, point)

    def __neg__(self) -> Piece:
        """Reflect the piece across the x-axis."""
        return _neg(self)

    def __matmul__(self, angle: sp.Expr) -> Piece:
        """Rotate the piece wrt to the origin."""
        return _rotate(self, angle)

    def reflect(self, axis: Literal["x", "y"]) -> Piece:
        """Reflect the piece across the real axis."""
        return _reflect(self, axis=axis)

    def get_all_variations(self, *, optimize: bool = False) -> list[Piece]:
        """Return all possible variations of the piece."""
        return _get_all_variations(self, optimize=optimize)
