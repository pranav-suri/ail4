from collections import defaultdict

def print_graph(adj_list: defaultdict[str, list], nodes: set):
    print("Adjacency list:")
    for node in sorted(nodes):
        print(f"{node}: {adj_list.get(node, [])}")

def add_undirected_edge(adj_list: defaultdict[str, list], u, v, nodes: set):
    adj_list[u].append(v)
    adj_list[v].append(u)
    nodes.add(u)
    nodes.add(v)

def build_graph_from_user_input():
    adj_list = defaultdict(list)
    nodes = set()
    while True:
        edge = input("Enter an edge (u v) or 'done' to finish: ")
        if edge.lower() == 'done':
            break
        u, v = edge.split()
        add_undirected_edge(adj_list, u, v, nodes)
    return adj_list, nodes

def dfs_iterative(start_node, adj_list: defaultdict[str, list], visited: set):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in adj_list.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

def DFS(start_node: str, adj_list: defaultdict[str, list]):
    print("\nDFS Iterative:")
    visited = set()
    dfs_iterative(start_node, adj_list, visited)

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
    # adj_list, nodes = build_graph_from_user_input()
    print_graph(adj_list, nodes)
    DFS('A', adj_list)    

main()