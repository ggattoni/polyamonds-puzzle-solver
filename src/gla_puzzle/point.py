from __future__ import annotations

from dataclasses import dataclass
from functools import cache

import sympy as sp

X_UNIT = sp.Integer(1)
Y_UNIT = sp.sqrt(3) / 2


@cache
def _add(a: Point, b: Point) -> Point:
    """Translate the point by another point."""
    return Point(a.x + b.x, a.y + b.y)


@cache
def _sub(a: Point, b: Point) -> Point:
    """Translate the point by another point."""
    return Point(a.x - b.x, a.y - b.y)


@cache
def _neg(point: Point) -> Point:
    """Negate the point."""
    return Point(-point.x, -point.y)


@cache
def _rotate(point: Point, angle: sp.Expr) -> Point:
    """Rotate the point wrt to the origin."""
    return Point(
        point.x * sp.cos(angle) - point.y * sp.sin(angle),
        point.x * sp.sin(angle) + point.y * sp.cos(angle),
    )


@dataclass
class Point:
    """Point class."""

    x: sp.Expr
    y: sp.Expr

    def __add__(self, other: Point) -> Point:
        """Translate the point by another point."""
        return _add(self, other)

    def __sub__(self, other: Point) -> Point:
        """Translate the point by another point."""
        return _sub(self, other)

    def __matmul__(self, angle: sp.Expr) -> Point:
        """Rotate the point wrt to the origin."""
        return _rotate(self, angle)

    def __neg__(self) -> Point:
        """Negate the point."""
        return _neg(self)

    def __eq__(self, value: Point) -> bool:
        """Check if two points are equal."""
        return self.x == value.x and self.y == value.y

    def __hash__(self) -> int:
        """Return the hash of the point."""
        return hash((self.x, self.y))
