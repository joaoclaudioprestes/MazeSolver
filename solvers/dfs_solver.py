class DFSSolver:
    def __init__(self, graph):
        self.graph = graph

    def solve(self, start, end):
        visited = set()
        path = []

        def dfs(node):
            visited.add(node)
            path.append(node)

            if node == end:
                return True

            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            path.pop()
            return False

        found = dfs(start)
        return path if found else None
