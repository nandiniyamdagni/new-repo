from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def dfs(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)
    
    def connected_components(self):
        visited = [False] * self.V
        components = []
        for v in range(self.V):
            if not visited[v]:
                component = []
                self.dfs(v, visited, component)
                components.append(component)
        return components

# Example usage:
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(5, 6)

components = g.connected_components()
print("Connected Components:")
for idx, c in enumerate(components):
    print(f"Component {idx + 1}: {c}")

