"""Triangle implementation."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache, cached_property
from statistics import mode
from typing import Literal

from gla_puzzle.point import Point


@cache
def _add(triangle: Triangle, point: Point) -> Triangle:
    """Translate the triangle by a point."""
    return Triangle(triangle.a + point, triangle.b + point, triangle.c + point)


@cache
def _sub(triangle: Triangle, point: Point) -> Triangle:
    """Translate the triangle by a point."""
    return Triangle(triangle.a - point, triangle.b - point, triangle.c - point)


@cache
def _neg(triangle: Triangle) -> Triangle:
    """Negate the triangle."""
    return Triangle(-triangle.a, -triangle.b, -triangle.c)


@cache
def _rotate(triangle: Triangle, angle: float) -> Triangle:
    """Rotate the triangle wrt to the origin."""
    return Triangle(triangle.a @ angle, triangle.b @ angle, triangle.c @ angle)


@cache
def _reflect(triangle: Triangle, axis: Literal["x", "y"]) -> Triangle:
    """Reflect the triangle wrt to the x-axis."""
    return Triangle(
        Point(triangle.a.x if axis == "x" else -triangle.a.x, triangle.a.y if axis == "y" else -triangle.a.y),
        Point(triangle.b.x if axis == "x" else -triangle.b.x, triangle.b.y if axis == "y" else -triangle.b.y),
        Point(triangle.c.x if axis == "x" else -triangle.c.x, triangle.c.y if axis == "y" else -triangle.c.y),
    )


@dataclass
class Triangle:
    """Triangle class."""

    a: Point
    b: Point
    c: Point

    @cached_property
    def center(self) -> Point:
        """Return the center of the triangle."""
        return Point(
            (max(self.a.x, self.b.x, self.c.x) + min(self.a.x, self.b.x, self.c.x)) / 2,
            (max(self.a.y, self.b.y, self.c.y) + min(self.a.y, self.b.y, self.c.y)) / 2,
        )

    def __add__(self, other: Point) -> Triangle:
        """Translate the triangle by a point."""
        return _add(self, other)

    def __sub__(self, other: Point) -> Triangle:
        """Translate the triangle by a point."""
        return _sub(self, other)

    def __matmul__(self, angle: float) -> Triangle:
        """Rotate the triangle wrt to the origin."""
        return _rotate(self, angle)

    def __neg__(self) -> Triangle:
        """Negate the triangle."""
        return _neg(self)

    def __eq__(self, other: Triangle) -> bool:
        """Check if two triangles are equal."""
        # return self.center == value.center
        other_points = (other.a, other.b, other.c)
        return self.a in other_points and self.b in other_points and self.c in other_points

    def __hash__(self) -> int:
        """Return the hash of the triangle."""
        return hash(frozenset([self.a, self.b, self.c]))

    @cached_property
    def up(self) -> bool:
        """Check if the triangle is pointing up."""
        return mode((self.a.y, self.b.y, self.c.y)) == min(self.a.y, self.b.y, self.c.y)

    @cached_property
    def down(self) -> bool:
        """Check if the triangle is pointing down."""
        return mode((self.a.y, self.b.y, self.c.y)) == max(self.a.y, self.b.y, self.c.y)

    def reflect(self, axis: Literal["x", "y"]) -> Triangle:
        """Reflect the triangle wrt to the x-axis."""
        return _reflect(self, axis=axis)
