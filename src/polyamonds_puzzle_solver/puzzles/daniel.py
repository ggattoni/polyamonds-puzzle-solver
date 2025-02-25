from polyamonds_puzzle_solver.grid import Grid, create_triangle_line
from polyamonds_puzzle_solver.piece import Piece
from polyamonds_puzzle_solver.point import Point
from polyamonds_puzzle_solver.triangle import Triangle

D_PIECE = Piece(
    name="D",
    triangles={
        Triangle(
            Point(-1, 1),
            Point(0, 0),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 0),
            Point(1, 1),
            Point(2, 0),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 0),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 0),
            Point(3, 1),
            Point(4, 0),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 0),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 0),
            Point(5, 1),
            Point(6, 0),
        ),
        Triangle(
            Point(5, 1),
            Point(6, 0),
            Point(7, 1),
        ),
        Triangle(
            Point(5, 1),
            Point(7, 1),
            Point(6, 2),
        ),
        Triangle(
            Point(5, 1),
            Point(6, 2),
            Point(4, 2),
        ),
        Triangle(
            Point(-1, 1),
            Point(1, 1),
            Point(0, 2),
        ),
        Triangle(
            Point(-1, 1),
            Point(0, 2),
            Point(-2, 2),
        ),
        Triangle(
            Point(-2, 2),
            Point(-1, 3),
            Point(0, 2),
        ),
        Triangle(
            Point(-1, 3),
            Point(0, 2),
            Point(1, 3),
        ),
        Triangle(
            Point(0, 2),
            Point(1, 3),
            Point(2, 2),
        ),
        Triangle(
            Point(1, 3),
            Point(2, 2),
            Point(3, 3),
        ),
        Triangle(
            Point(2, 2),
            Point(3, 3),
            Point(4, 2),
        ),
        Triangle(
            Point(3, 3),
            Point(4, 2),
            Point(5, 3),
        ),
        Triangle(
            Point(4, 2),
            Point(5, 3),
            Point(6, 2),
        ),
        Triangle(
            Point(-1, 3),
            Point(-2, 2),
            Point(-3, 3),
        ),
    },
)

A_PIECE = Piece(
    name="A",
    triangles={
        Triangle(
            Point(-1, 1),
            Point(0, 0),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 0),
            Point(1, 1),
            Point(2, 0),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 0),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 0),
            Point(3, 1),
            Point(4, 0),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 0),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 0),
            Point(5, 1),
            Point(6, 0),
        ),
        Triangle(
            Point(5, 1),
            Point(6, 0),
            Point(7, 1),
        ),
        Triangle(
            Point(6, 0),
            Point(7, 1),
            Point(8, 0),
        ),
        Triangle(
            Point(-1, 1),
            Point(0, 2),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 2),
            Point(1, 1),
            Point(2, 2),
        ),
        Triangle(
            Point(0, 2),
            Point(2, 2),
            Point(1, 3),
        ),
        Triangle(
            Point(2, 2),
            Point(1, 3),
            Point(3, 3),
        ),
        Triangle(
            Point(1, 3),
            Point(3, 3),
            Point(2, 4),
        ),
        Triangle(
            Point(3, 3),
            Point(2, 4),
            Point(4, 4),
        ),
        Triangle(
            Point(3, 5),
            Point(2, 4),
            Point(4, 4),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 2),
            Point(5, 1),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 2),
            Point(2, 2),
        ),
        Triangle(
            Point(3, 3),
            Point(4, 2),
            Point(2, 2),
        ),
    },
)

N_PIECE = Piece(
    name="N",
    triangles={
        Triangle(
            Point(-1, 1),
            Point(0, 0),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 0),
            Point(1, 1),
            Point(2, 0),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 0),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 0),
            Point(3, 1),
            Point(4, 0),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 0),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 0),
            Point(5, 1),
            Point(6, 0),
        ),
        Triangle(
            Point(-1, 1),
            Point(0, 2),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 2),
            Point(1, 1),
            Point(2, 2),
        ),
        Triangle(
            Point(-3, 3),
            Point(-2, 2),
            Point(-1, 3),
        ),
        Triangle(
            Point(-2, 2),
            Point(-1, 3),
            Point(0, 2),
        ),
        Triangle(
            Point(-1, 3),
            Point(0, 2),
            Point(1, 3),
        ),
        Triangle(
            Point(0, 2),
            Point(1, 3),
            Point(2, 2),
        ),
        Triangle(
            Point(1, 3),
            Point(2, 2),
            Point(3, 3),
        ),
        Triangle(
            Point(2, 2),
            Point(3, 3),
            Point(4, 2),
        ),
    },
)

I_PIECE = Piece(
    name="I",
    triangles={
        Triangle(
            Point(0, 0),
            Point(2, 0),
            Point(1, 1),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 0),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 0),
            Point(3, 1),
            Point(4, 0),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 0),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 0),
            Point(5, 1),
            Point(6, 0),
        ),
        Triangle(
            Point(5, 1),
            Point(6, 0),
            Point(7, 1),
        ),
        # Triangle(
        #     Point(6, 0),
        #     Point(7, 1),
        #     Point(8, 0),
        # ),
    },
)

E_PIECE = Piece(
    name="E",
    triangles={
        Triangle(
            Point(-2, 0),
            Point(-1, 1),
            Point(0, 0),
        ),
        Triangle(
            Point(-1, 1),
            Point(0, 0),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 0),
            Point(1, 1),
            Point(2, 0),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 0),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 0),
            Point(3, 1),
            Point(4, 0),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 0),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 0),
            Point(5, 1),
            Point(6, 0),
        ),
        Triangle(
            Point(5, 1),
            Point(6, 0),
            Point(7, 1),
        ),
        Triangle(
            Point(6, 0),
            Point(7, 1),
            Point(8, 0),
        ),
        Triangle(
            Point(7, 1),
            Point(8, 0),
            Point(9, 1),
        ),
        Triangle(
            Point(7, 1),
            Point(9, 1),
            Point(8, 2),
        ),
        Triangle(
            Point(9, 1),
            Point(8, 2),
            Point(10, 2),
        ),
        Triangle(
            Point(-1, 1),
            Point(0, 2),
            Point(1, 1),
        ),
        Triangle(
            Point(0, 2),
            Point(1, 1),
            Point(2, 2),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 2),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 2),
            Point(5, 1),
            Point(6, 2),
        ),
        Triangle(
            Point(0, 2),
            Point(1, 3),
            Point(2, 2),
        ),
        Triangle(
            Point(4, 2),
            Point(5, 3),
            Point(6, 2),
        ),
        Triangle(
            Point(8, 2),
            Point(9, 3),
            Point(10, 2),
        ),
    },
)

L_PIECE = Piece(
    name="L",
    triangles={
        Triangle(
            Point(0, 0),
            Point(1, 1),
            Point(2, 0),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 0),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 0),
            Point(3, 1),
            Point(4, 0),
        ),
        Triangle(
            Point(3, 1),
            Point(4, 0),
            Point(5, 1),
        ),
        Triangle(
            Point(4, 0),
            Point(5, 1),
            Point(6, 0),
        ),
        Triangle(
            Point(1, 1),
            Point(2, 2),
            Point(3, 1),
        ),
        Triangle(
            Point(2, 2),
            Point(3, 1),
            Point(4, 2),
        ),
        Triangle(
            Point(2, 2),
            Point(4, 2),
            Point(3, 3),
        ),
        Triangle(
            Point(4, 2),
            Point(3, 3),
            Point(5, 3),
        ),
        Triangle(
            Point(3, 3),
            Point(5, 3),
            Point(4, 4),
        ),
        Triangle(
            Point(5, 3),
            Point(4, 4),
            Point(6, 4),
        ),
    },
)

PIECES = [D_PIECE, A_PIECE, N_PIECE, I_PIECE, E_PIECE, L_PIECE]

triangles = []
up_triangles = [13, 15, 17]
up_leftmost_points = [
    Point(-7, 3),
    Point(-8, 2),
    Point(-9, 1),
]
for num_triangles, leftmost_point in zip(up_triangles, up_leftmost_points, strict=False):
    triangles.extend(create_triangle_line(num_triangles=num_triangles, leftmost_point=leftmost_point, up=True))

down_triangles = [17, 15, 13, 11]
down_leftmost_points = [
    Point(-9, 1),
    Point(-8, 0),
    Point(-7, -1),
    Point(-6, -2),
]
for num_triangles, leftmost_point in zip(down_triangles, down_leftmost_points, strict=False):
    triangles.extend(create_triangle_line(num_triangles=num_triangles, leftmost_point=leftmost_point, up=False))

GRID = Grid(triangles)
