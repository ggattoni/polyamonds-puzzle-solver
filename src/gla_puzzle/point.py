from __future__ import annotations

from dataclasses import dataclass
from functools import cache, cached_property
from math import cos, sin, sqrt

X_UNIT = 0.5
Y_UNIT = sqrt(3) / 2


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
def _rotate(point: Point, angle: float) -> Point:
    """Rotate the point wrt to the origin."""
    return Point(
        round((point.x * X_UNIT * cos(angle) - point.y * Y_UNIT * sin(angle)) / X_UNIT),
        round((point.x * X_UNIT * sin(angle) + point.y * Y_UNIT * cos(angle)) / Y_UNIT),
    )


@dataclass
class Point:
    """Point class."""

    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        """Translate the point by another point."""
        return _add(self, other)

    def __sub__(self, other: Point) -> Point:
        """Translate the point by another point."""
        return _sub(self, other)

    def __matmul__(self, angle: float) -> Point:
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

    @cached_property
    def coordinates(self) -> tuple[float, float]:
        """Return the coordinates of the point."""
        return self.x * X_UNIT, self.y * Y_UNIT
