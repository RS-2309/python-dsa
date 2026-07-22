class DirectedGraph:
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
        raise NotImplementedError(
            "Directed graphs use weakly/strongly connected."
        )

    def is_weakly_connected(self):
        if not self.graph:
            return True

        temp = {v: [] for v in self.graph}

        for source in self.graph:
            for destination in self.graph[source]:
                temp[source].append(destination)
                temp[destination].append(source)

        stack = [next(iter(temp))]
        visited = set()

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)

            for neighbor in temp[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return len(visited) == len(self.graph)
    
    def is_strongly_connected(self):

        for vertex in self.graph:

            if len(self.bfs(vertex).order) != len(self.graph):
                return False

        return True

    def add_vertex(self, vertex: str):
        if vertex in self.graph:
            return f"Vertex: '{vertex}' already exists."
        
        self.graph[vertex] = []

        self.canuse = False
        self.bfspair = None

        return []

    def add_edge(self, source: str, destination: str):
        if source not in self.graph:
            raise KeyError(source)
        
        if destination not in self.graph:
            raise KeyError(destination)
        
        if destination not in self.graph[source]:
            self.graph[source].append(destination)
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
                self.edges -= 1

        self.canuse = False
        self.bfspair = None

    def remove_edge(self, source: str, destination: str):
        if source not in self.graph:
            raise KeyError(source)
        
        if destination not in self.graph:
            raise KeyError(destination)

        if destination not in self.graph[source]:
            raise KeyError(f"Edge {source, destination} does not exist.")

        if destination in self.graph[source]:
            self.graph[source].remove(destination)
            self.edges -= 1
            self.canuse = False
            self.bfspair = None

    def has_vertex(self, vertex: str):
        if vertex in self.graph:
            return True
        
        return False

    def has_edge(self, source: str, destination: str):
        if source not in self.graph:
            raise KeyError(source)

        if destination not in self.graph:
            raise KeyError(destination)

        if destination in self.graph[source]:
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