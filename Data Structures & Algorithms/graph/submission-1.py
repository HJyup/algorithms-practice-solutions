class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque()
        visited = set()

        queue.append(src)
        visited.add(src)

        while queue:
            q_l = len(queue)
            for i in range(q_l):
                curr = queue.popleft()
                if curr == dst:
                    return True
                
                for nb in self.adj_list[curr]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)

        return False

