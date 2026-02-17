import random
import networkx as nx


class Maze:
    def __init__(self, size, labyrinth="matrix"):
        self.size = size
        self.labyrinth = labyrinth

    def generate_labyrinth(self):
        graph = self.generate_graph_labyrinth(self.size)
        return graph

    def generate_graph_labyrinth(self, size):
        print("Generating graph labyrinth...")

        graph = nx.Graph()

        # Add nodes to the graph
        for i in range(size):
            for j in range(size):
                graph.add_node((i, j))

        # Connect nodes in a grid pattern
        for i in range(size):
            for j in range(size):
                if i < size - 1:
                    graph.add_edge((i, j), (i + 1, j))
                if j < size - 1:
                    graph.add_edge((i, j), (i, j + 1))

        return graph
