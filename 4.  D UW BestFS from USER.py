from collections import defaultdict
from queue import PriorityQueue

def print_graph(adj_list: defaultdict[str, list[str]], nodes: set):
    print("Adjacency list")
    for node in sorted(nodes):
        print(f"{node}: {adj_list.get(node, [])}")

def add_directed_edge(adj_list: defaultdict[str, list[str]], u, v, nodes: set):
    adj_list[u].append(v)
    nodes.add(u)
    nodes.add(v)

def build_graph_from_user():
    adj_list = defaultdict(list)
    nodes = set()

    while True:
        edge = input("Enter an edge (u v) or 'done' to finish: ")
        if edge.lower() == "done":
            break
        u, v = edge.split()
        add_directed_edge(adj_list, u, v, nodes)

    return adj_list, nodes

def get_heurictics_from_user(nodes: set):
    heuristics = {}
    for node in sorted(nodes):
        val = input(f"Enter heuristic value for node {node}: ")
        heuristics[node] = int(val)

    return heuristics

def reconstruct_path(parent_map: dict, start_node, goal_node):
    path = []
    current = goal_node
    while current is not None:
        path.append(current)
        if current == start_node: # start_node reached
            break
        parent = parent_map.get(current)
        current = parent

    if path[-1] != start_node: # loop finished without reaching start_node
        return None

    return path[::-1] # reverse to get start to goal order

def best_first_search(adj_list: defaultdict[str, list[str]], heuristics: dict[str, int], start_node, goal_node):

    # stores tuples: (heuristic_value, node)
    pq: PriorityQueue[tuple[int, str]] = PriorityQueue()
    pq.put((heuristics[start_node], start_node))

    # stores {child: parent}
    parent_map: dict = {start_node: None}

    visited = set()

    while not pq.empty():
        current_h, current_node = pq.get()

        if current_node == goal_node:
            print("Goal reached")
            path = reconstruct_path(parent_map, start_node, goal_node)
            print("-" * 20)
            return path

        visited.add(current_node)
        neighbors = adj_list.get(current_node, [])
        for neighbor in neighbors:
            if neighbor not in parent_map:
                parent_map[neighbor] = current_node
                pq.put((heuristics[neighbor], neighbor))
    print("Goal not reachable.")

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
    heuristics = {
        'A': 10,
        'B': 7,
        'C': 8,
        'D': 3,
        'E': 5,
        'F': 0  # goal
    }

    for u, v in edges:
        add_directed_edge(adj_list,u,v,nodes)

    return adj_list, nodes, heuristics
    
def main():
    adj_list, nodes, heuristics = test_values()
    # adj_list, nodes = build_graph_from_user()
    # heuristics = get_heurictics_from_user()

    start_node = 'A'
    goal_node = 'F'

    path = best_first_search(adj_list, heuristics, start_node, goal_node)
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found.")

main()
