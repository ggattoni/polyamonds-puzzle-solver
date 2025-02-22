from pathlib import Path

import numpy as np
from ortools.sat.python import cp_model
from tqdm import tqdm

from polyamonds_puzzle_solver.grid import Grid
from polyamonds_puzzle_solver.piece import Piece
from polyamonds_puzzle_solver.plot import plot_grid
from polyamonds_puzzle_solver.point import Point


class SolutionStore(cp_model.CpSolverSolutionCallback):
    """Store solutions."""

    def __init__(self, variables: list[cp_model.IntVar]) -> None:
        """Initialize the solution store."""
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.__solutions = []

    def on_solution_callback(self) -> None:
        """Store the solution."""
        self.__solution_count += 1
        solution = tuple(sorted([i for i, v in enumerate(self.__variables) if self.Value(v) == 1]))
        self.__solutions.append(solution)

    @property
    def solution_count(self) -> int:
        """Return the number of solutions."""
        return self.__solution_count

    @property
    def solutions(self) -> list[tuple[int]]:
        """Return the solutions."""
        return self.__solutions


def solve(grid: Grid, pieces: list[Piece], folder: Path | None = None, *, verbose: bool = False) -> None:
    """Solve the puzzle."""
    num_cells = len(grid.triangles)
    num_pieces = len(pieces)
    num_columns = num_cells + num_pieces

    row_piece_mapping = {}
    rows = []
    row_counter = 0

    for piece_counter, piece in tqdm(enumerate(pieces), leave=False, position=0):
        for variation in tqdm(piece.get_all_variations(), leave=False, position=1):
            for point in tqdm(grid.available_points(variation), leave=False, position=2):
                row = np.zeros(num_columns, dtype=int)
                translation = variation + point
                indexes = [grid.integer_mapping[triangle] for triangle in translation.triangles]
                row[indexes] = 1
                row[num_cells + piece_counter] = 1
                rows.append(row)
                row_piece_mapping[row_counter] = translation
                row_counter += 1

    incidence_matrix = np.array(rows)

    model = cp_model.CpModel()

    # Create variables
    variables = [model.new_bool_var(f"{row}") for row in range(incidence_matrix.shape[0])]

    # Create constraints
    for column in range(num_cells):
        model.add(sum(incidence_matrix[row, column] * variables[row] for row in range(incidence_matrix.shape[0])) <= 1)
    for column in range(num_cells, num_columns):
        model.add(sum(incidence_matrix[row, column] * variables[row] for row in range(incidence_matrix.shape[0])) == 1)

    solver = cp_model.CpSolver()
    solution_store = SolutionStore(variables)
    solver.parameters.max_time_in_seconds = 60
    solver.parameters.enumerate_all_solutions = True
    status = solver.solve(model, solution_callback=solution_store)

    if verbose:
        print(f"Status: {solver.status_name(status)}")
        print(f"Conflicts: {solver.num_conflicts}")
        print(f"Branches : {solver.num_branches}")
        print(f"Wall time: {solver.wall_time} s")
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            print(f"# Solutions found: {solution_store.solution_count}")
        else:
            print("No solution found.")

    for solution in solution_store.solutions:
        solved_grid = grid
        for i in solution:
            solved_grid = solved_grid.place_piece(row_piece_mapping[i], Point(0, 0))
        plot_grid(solved_grid, folder=folder)
