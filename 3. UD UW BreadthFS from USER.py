from collections import defaultdict
from collections import deque

def print_graph(adj_list: defaultdict[str, list], nodes: set):
    print("Adjacency list:")
    for node in sorted(nodes):
        print(f"{node}: {adj_list.get(node, [])}")

def add_undirected_edge(adj_list: defaultdict[str, list], u, v, nodes: set):
    adj_list[u].append(v)
    adj_list[v].append(u)
    nodes.add(u)
    nodes.add(v)

def build_graph_from_user():
    adj_list = defaultdict(list)
    nodes = set()
    while True:
        edge = input("Enter an edge (u v) or 'done' to finish: ")
        if edge.lower() == 'done':
            break
        u, v = edge.split()
        add_undirected_edge(adj_list, u, v, nodes)
    return adj_list, nodes

def bfs(start_node, adj_list: defaultdict[str, list], visited: set):
    queue = deque([start_node])
    visited = {start_node}
    print(f"\nBFS starting from node: {start_node}")

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def test_values():
    adj_list = defaultdict(list)
    nodes = set()
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('C', 'E'),
        ('D', 'F'),
        ('E', 'F') 
    ]

    for u, v in edges:
        add_undirected_edge(adj_list,u,v,nodes)

    return adj_list, nodes


def main():
    adj_list, nodes = test_values()
    # adj_list, nodes = build_graph_from_user()
    print_graph(adj_list, nodes)
    bfs('A', adj_list, nodes)

main()