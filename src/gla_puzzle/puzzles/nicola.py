import sympy as sp

from gla_puzzle import X_UNIT, Y_UNIT, Grid, Piece, Point, Triangle, create_triangle_line

N_PIECE = Piece(
    name="N",
    triangles={
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(1 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(1 * X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(1 * X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(1 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(1 * X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(-3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(-X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT / 2, 3 * Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, 3 * Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(1 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(1 * X_UNIT / 2, 3 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(1 * X_UNIT / 2, 3 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
        ),
    },
)

I_PIECE = Piece(
    name="I",
    triangles={
        Triangle(
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT, 0 * Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
            Point(4 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(7 * X_UNIT / 2, Y_UNIT),
            Point(4 * X_UNIT, 0 * Y_UNIT),
            Point(9 * X_UNIT / 2, Y_UNIT),
        ),
    },
)

C_PIECE = Piece(
    name="C",
    triangles={
        Triangle(
            Point(-X_UNIT, 2 * Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT, 2 * Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT / 2, Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(7 * X_UNIT / 2, Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 2 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT, 2 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
        ),
    },
)

O_PIECE = Piece(
    name="O",
    triangles={
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 2 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT, 2 * Y_UNIT),
            Point(-X_UNIT / 2, 3 * Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, 3 * Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT / 2, 3 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, 3 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
            Point(3 * X_UNIT, 2 * Y_UNIT),
        ),
    },
)

L_PIECE = Piece(
    name="L",
    triangles={
        Triangle(
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 2 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
            Point(2 * X_UNIT, 4 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, 3 * Y_UNIT),
            Point(2 * X_UNIT, 4 * Y_UNIT),
            Point(3 * X_UNIT, 4 * Y_UNIT),
        ),
    },
)

A_PIECE = Piece(
    name="A",
    triangles={
        Triangle(
            Point(-1 * X_UNIT, 0 * Y_UNIT),
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 0 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 0 * Y_UNIT),
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(2 * X_UNIT, 0 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(5 * X_UNIT / 2, Y_UNIT),
            Point(3 * X_UNIT, 0 * Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT, 0 * Y_UNIT),
            Point(7 * X_UNIT / 2, Y_UNIT),
            Point(4 * X_UNIT, 0 * Y_UNIT),
        ),
        Triangle(
            Point(-X_UNIT / 2, Y_UNIT),
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT / 2, Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(0 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT / 2, 3 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
        ),
        Triangle(
            Point(X_UNIT / 2, 3 * Y_UNIT),
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(X_UNIT, 4 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(X_UNIT, 4 * Y_UNIT),
            Point(2 * X_UNIT, 4 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, 5 * Y_UNIT),
            Point(X_UNIT, 4 * Y_UNIT),
            Point(2 * X_UNIT, 4 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(5 * X_UNIT / 2, Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
        ),
        Triangle(
            Point(3 * X_UNIT / 2, 3 * Y_UNIT),
            Point(2 * X_UNIT, 2 * Y_UNIT),
            Point(X_UNIT, 2 * Y_UNIT),
        ),
    },
)


PIECES = [N_PIECE, I_PIECE, C_PIECE, O_PIECE, L_PIECE, A_PIECE]

triangles = []
up_triangles = [13, 15, 17]
up_leftmost_points = [
    Point(sp.Rational(-7, 2) * X_UNIT, 3 * Y_UNIT),
    Point(sp.Integer(-4) * X_UNIT, 2 * Y_UNIT),
    Point(sp.Rational(-9, 2) * X_UNIT, 1 * Y_UNIT),
]
for num_triangles, leftmost_point in zip(up_triangles, up_leftmost_points, strict=False):
    triangles.extend(create_triangle_line(num_triangles=num_triangles, leftmost_point=leftmost_point, up=True))

down_triangles = [17, 15, 13, 11]
down_leftmost_points = [
    Point(sp.Rational(-9, 2) * X_UNIT, 1 * Y_UNIT),
    Point(sp.Integer(-4) * X_UNIT, 0 * Y_UNIT),
    Point(sp.Rational(-7, 2) * X_UNIT, -1 * Y_UNIT),
    Point(sp.Integer(-3) * X_UNIT, -2 * Y_UNIT),
    Point(sp.Rational(-5, 2) * X_UNIT, -3 * Y_UNIT),
]
for num_triangles, leftmost_point in zip(down_triangles, down_leftmost_points, strict=False):
    triangles.extend(create_triangle_line(num_triangles=num_triangles, leftmost_point=leftmost_point, up=False))

GRID = Grid(triangles)

__all__ = [
    "A_PIECE",
    "C_PIECE",
    "GRID",
    "I_PIECE",
    "L_PIECE",
    "N_PIECE",
    "O_PIECE",
    "PIECES",
]
