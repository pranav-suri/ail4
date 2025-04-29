from collections import defaultdict
import csv

def print_graph(adj_list: defaultdict[str, list], nodes: set):
    print("Adjacency list:")
    for node in sorted(nodes):
        print(f"{node}: {adj_list.get(node, [])}")

def add_undirected_edge(adj_list: defaultdict[str, list], u, v, nodes: set):
    adj_list[u].append(v)
    adj_list[v].append(u)
    nodes.add(u)
    nodes.add(v)

def build_graph_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        # header = next(reader) # skip header
        adj_list = defaultdict(list)
        nodes = set()

        for row in reader:
            u, v = row[0], row[1]
            add_undirected_edge(adj_list, u, v, nodes)

        return adj_list, nodes

def dfs_recursive(node, adj_list: defaultdict[str, list], visited: set):
    if node in visited:
        return
    visited.add(node)
    print(node, end=' ')
    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            dfs_recursive(neighbor, adj_list, visited)

def DFS(start_node: str, adj_list: defaultdict[str, list], nodes: set):
    print("\nDFS Recursive:")
    visited = set()
    print(f"Starting DFS from node: {start_node}")
    dfs_recursive(start_node, adj_list, visited)

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
    # adj_list, nodes = build_graph_from_csv('edges.csv')
    print_graph(adj_list, nodes)
    DFS('A', adj_list, nodes)

main()