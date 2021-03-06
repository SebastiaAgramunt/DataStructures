from typing import List, Dict

GraphType = Dict[str, List[str]]


class Node:
    # Node == Vertex of the graph
    def __init__(self, val: str, visited: bool = False):
        self.val = val
        self.visited = visited


NodesList = Dict[str, Node]


def get_nodes(graph: GraphType) -> NodesList:
    # from a Graph calculate a dictionary of all the vertices
    # with value an object Graph initialized as visited=False
    nodes = {}
    for vertex in graph:
        nodes[vertex] = Node(vertex)
        for vertex2 in graph[vertex]:
            nodes[vertex2] = Node(vertex2)

    return nodes


class Queue:
    # simple queue impolementation in python
    def __init__(self):
        self.queue = []

    def add(self, val):
        self.queue.append(val)

    def pop(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            self.queue = self.queue[1:]
            return val
        return None

    def isEmpty(self) -> bool:
        return True if len(self.queue) == 0 else False


def bfs(graph: GraphType, start: str) -> None:
    """Breadth First Search to transverse a graph
    Input:
        - graph: a GraphType indicating the connected nodes
        - start: a starting point to transverse all the graph
    """
    nodes = get_nodes(graph)
    queue = Queue()

    queue.add(start)

    while not queue.isEmpty():
        node = queue.pop()
        if not nodes[node].visited:
            nodes[node].visited = True
            for neighbor in graph[node]:
                queue.add(neighbor)
            print(f"Node {node} visited, Queue: {queue.queue}")


if __name__ == "__main__":
    graph: GraphType = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["A", "F"],
        "E": ["F"],
        "F": ["G"],
        "G": [],
        "H": ["B"],
    }

    # transverse from start_node all the graph
    # visit all nodes that you can
    start_node = "A"
    bfs(graph, start_node)
