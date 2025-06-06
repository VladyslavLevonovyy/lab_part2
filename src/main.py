import csv
from collections import defaultdict


def read_data(filename):
    edges = []
    nodes = set()
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue
                a, b, dist_str = row
                try:
                    dist = int(dist_str)
                    edges.append((dist, a, b))
                    nodes.add(a)
                    nodes.add(b)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    return edges, nodes


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y:
        return False
    parent[root_y] = root_x
    return True


def bubble_sort_edges(edges):
    n = len(edges)
    for i in range(n):
        for j in range(0, n - i - 1):
            if edges[j][0] > edges[j + 1][0]:
                edges[j], edges[j + 1] = edges[j + 1], edges[j]


def build_weighted_tree(mst):
    tree = defaultdict(list)
    for weight, a, b in mst:
        tree[a].append((b, weight))
        tree[b].append((a, weight))
    return tree


def print_weighted_tree(tree, root, visited=None, prefix=""):
    if visited is None:
        visited = set()
    visited.add(root)
    print(prefix + root)
    children = [(node, w) for node, w in tree[root] if node not in visited]
    for i, (child, weight) in enumerate(children):
        is_last = i == len(children) - 1
        new_prefix = prefix + ("    " if is_last else "│   ")
        branch = "└── " if is_last else "├── "
        print(prefix + branch + f"{child} ({weight})")
        print_weighted_tree(tree, child, visited, new_prefix)


def minimum_cable_length(filename):
    edges, nodes = read_data(filename)

    if not edges or not nodes:
        print("Дані не зчитано.")
        return -1

    print("Граф до алгоритму :")
    for dist, a, b in edges:
        print(f"{a} -- {dist} -- {b}")

    parent = {node: node for node in nodes}
    bubble_sort_edges(edges)

    total = 0
    count = 0
    mst = []

    for dist, a, b in edges:
        if union(parent, a, b):
            total += dist
            count += 1
            mst.append((dist, a, b))

    if count != len(nodes) - 1:
        print("\nПомилка: граф не є зв'язним — MST не побудовано.")
        return -1

    print("\nГраф після алгоритму :")
    tree = build_weighted_tree(mst)
    root = next(iter(tree))
    print_weighted_tree(tree, root)

    return total


if __name__ == "__main__":
    result = minimum_cable_length("connect.csv")
    if result != -1:
        print("\nМінімальна довжина кабелю:", result)
