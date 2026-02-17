import random
import time
from maze import Maze
from solvers.dfs_solver import DFSSolver
from solvers.bfs_solver import BFSSolver
from solvers.a_star import AStarSolver
from visualization.graph_plot import plot_graph_path


def main():
    size = random.randint(5, 10)
    maze = Maze(size)
    maze.labyrinth = "graph"
    graph = maze.generate_labyrinth()

    start = (0, 0)
    end = (size - 1, size - 1)

    solvers = [DFSSolver(graph), BFSSolver(graph), AStarSolver(graph)]

    for solver in solvers:
        start_time = time.time()
        path = solver.solve(start, end)
        end_time = time.time()

        found = path is not None
        print(
            f"{solver.__class__.__name__}: Found: {found}, Time: {end_time - start_time:.4f} seconds"
        )

        if found:
            plot_graph_path(graph, path=path, start=start, end=end)
        else:
            plot_graph_path(graph, start=start, end=end)


if __name__ == "__main__":
    main()
