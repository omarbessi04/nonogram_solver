from puzzlemaker import PuzzleMaker
from puzzlersolver import PuzzleSolver


def main():
    puzzle = PuzzleMaker.get_new_puzzle()
    solution = PuzzleSolver.solve_puzzle(puzzle)
    PuzzleSolver.show_solution(solution)
