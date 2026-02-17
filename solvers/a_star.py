class AStarSolver:
    def __init__(self, graph):
        self.graph = graph
        self.path = []

    def heuristic(self, node, end):
        # Heuristic function: Manhattan distance
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    def solve(self, start, end):
        open_set = set([start])
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}

        while open_set:
            # Node with the lowest f_score
            current = min(open_set, key=lambda x: f_score.get(x, float("inf")))

            # If current is the end node, reconstruct the path
            if current == end:
                self.path = []
                while current in came_from:
                    self.path.append(current)
                    current = came_from[current]
                self.path.append(start)
                self.path.reverse()
                return self.path

            open_set.remove(current)

            for neighbor in self.graph.neighbors(current):
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(
                        neighbor, end
                    )

                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return None
