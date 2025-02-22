from polyamonds_puzzle_solver import Grid, Piece, Point, Triangle, create_triangle_line

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
            Point(5, 1),
            Point(6, 0),
            Point(7, 1),
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

U_PIECE = Piece(
    name="U",
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
            Point(7, 1),
            Point(6, 2),
            Point(8, 2),
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
            Point(5, 3),
            Point(6, 2),
            Point(7, 3),
        ),
        Triangle(
            Point(6, 2),
            Point(7, 3),
            Point(8, 2),
        ),
        Triangle(
            Point(7, 3),
            Point(8, 2),
            Point(9, 3),
        ),
    },
)

C_PIECE = Piece(
    name="C",
    triangles={
        Triangle(
            Point(0, 2),
            Point(-1, 1),
            Point(-2, 2),
        ),
        Triangle(
            Point(0, 2),
            Point(-1, 1),
            Point(1, 1),
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
            Point(6, 2),
            Point(4, 2),
            Point(5, 3),
        ),
        Triangle(
            Point(4, 2),
            Point(5, 3),
            Point(3, 3),
        ),
    },
)

I_PIECE = Piece(
    name="I",
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
    },
)

A_PIECE = Piece(
    name="A",
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
    },
)

O_PIECE = Piece(
    name="O",
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
    },
)

PIECES = [L_PIECE, U_PIECE, C_PIECE, I_PIECE, A_PIECE, N_PIECE, O_PIECE]


triangles = []
up_triangles = [15, 17, 19]
up_leftmost_points = [
    Point(-8, 3),
    Point(-9, 2),
    Point(-10, 1),
]
for num_triangles, leftmost_point in zip(up_triangles, up_leftmost_points, strict=False):
    triangles.extend(create_triangle_line(num_triangles=num_triangles, leftmost_point=leftmost_point, up=True))

down_triangles = [19, 17, 15, 13]
down_leftmost_points = [
    Point(-10, 1),
    Point(-9, 0),
    Point(-8, -1),
    Point(-7, -2),
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
    "U_PIECE",
]
