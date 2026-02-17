from collections import deque


class BFSSolver:
    def __init__(self, graph):
        self.graph = graph

    def solve(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_node, path = queue.popleft()

            if current_node == end:
                return path

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None
