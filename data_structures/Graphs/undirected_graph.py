class UndirectedGraph:
    def __init__(self):
        self.graph = {}
        self.edges = 0
        self.bfspair = None
        self.canuse = False
        self.last_start = None

    def __iter__(self):
        return iter(self.graph)
    
    def __getitem__(self, key):
        return self.graph[key]

    def __contains__(self, vertex):
        if vertex in self.graph:
            return True
        
        return False

    def __repr__(self):
        return f"Graph({self.graph})"

    def __len__(self):
        return len(self.graph)

    def __str__(self):
        return (f"Vertices: {len(self.graph)}\n"
        f"Edges: {self.edges}\n"
        f"Graph: {self.graph}")
    
    def is_connected(self):
        if not self.graph:
            return True
        
        return len(self.bfs(next(iter(self.graph))).order) == len(self.graph)

    def add_vertex(self, vertex: str):
        if vertex in self.graph:
            return f"Vertex: '{vertex}' already exists."
        
        self.graph[vertex] = []

        self.canuse = False
        self.bfspair = None

        return []

    def add_edge(self, vertex_1: str, vertex_2: str):
        if vertex_1 not in self.graph:
            raise KeyError(vertex_1)
        
        if vertex_2 not in self.graph:
            raise KeyError(vertex_2)
        
        if vertex_2 not in self.graph[vertex_1]:
            self.graph[vertex_1].append(vertex_2)
        
        if vertex_1 not in self.graph[vertex_2]:
            self.graph[vertex_2].append(vertex_1)

        self.edges += 1
        self.canuse = False
        self.bfspair = None

    def remove_vertex(self, vertex: str):
        if vertex not in self.graph:
            raise KeyError(vertex)
        
        self.edges -= len(self.graph[vertex])
        self.graph.pop(vertex)

        for key in self.graph:
            if vertex in self.graph[key]:
                self.graph[key].remove(vertex)

        self.canuse = False
        self.bfspair = None
        

    def remove_edge(self, vertex_1: str, vertex_2: str):
        if vertex_1 not in self.graph:
            raise KeyError(vertex_1)
        
        if vertex_2 not in self.graph:
            raise KeyError(vertex_2)

        if vertex_2 not in self.graph[vertex_1]:
            raise KeyError(f"Edge {vertex_1, vertex_2} does not exist.")

        if vertex_2 in self.graph[vertex_1]:
            self.graph[vertex_1].remove(vertex_2)

        if vertex_1 in self.graph[vertex_2]:
            self.graph[vertex_2].remove(vertex_1)

        self.edges -= 1
        self.canuse = False
        self.bfspair = None

    def has_vertex(self, vertex: str):
        if vertex in self.graph:
            return True
        
        return False

    def has_edge(self, vertex_1: str, vertex_2: str):
        if vertex_1 not in self.graph:
            raise KeyError(vertex_1)

        if vertex_2 not in self.graph:
            raise KeyError(vertex_2)

        if vertex_2 in self.graph[vertex_1]:
            return True

        return False
    
    class BFSResult:
        def __init__(self, order, place_value):
            self.order = order
            self.place_value = place_value

        def __contains__(self, value):
            return value in self.order
        
        def __repr__(self):
            return (f"Order: {self.order},\
                    \nDistances: {self.place_value}")

    def bfs(self, start):
        if self.canuse and self.last_start == start:
            return self.BFSResult(self.bfspair[0], self.bfspair[1])

        queue = [start]
        visited = set()
        order = []
        place_value = {start: 0}

        while queue:
            current = queue.pop(0)

            if current in visited:
                continue
            
            visited.add(current)
            order.append(current)

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

            for key in queue:
                if key not in place_value:
                    place_value[key] = place_value[current] + 1

        self.bfspair = [order, place_value]
        self.canuse = True
        self.last_start = start

        return self.BFSResult(order, place_value)

    def dfs(self, start):
        stack = [start]
        visited = set()
        order = []

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            order.append(current)

            for neighbor in reversed(self.graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

        return order