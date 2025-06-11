class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
        else:
            self._insert(self.root, value, priority)

    def _insert(self, node, value, priority):
        if priority < node.priority:
            if not node.left:
                node.left = Node(value, priority)
            else:
                self._insert(node.left, value, priority)
        else:
            if not node.right:
                node.right = Node(value, priority)
            else:
                self._insert(node.right, value, priority)

    def get_highest_priority(self):
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def remove_highest_priority(self):
        if not self.root:
            return None
        self.root, value = self._remove(self.root)
        return value

    def _remove(self, node):
        if not node.left:
            return node.right, node.value
        node.left, value = self._remove(node.left)
        return node, value

    def print_queue(self):
        self._print_in_order(self.root)
        print()

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(f'({node.value}, {node.priority})', end=' ')
            self._print_in_order(node.right)


pq = PriorityQueue()
pq.insert("A", 3)
pq.insert("B", 1)
pq.insert("C", 2)

pq.print_queue()
print("Найвищий пріоритет має:", pq.get_highest_priority())
print("Видалено найвищий пріоритет:", pq.remove_highest_priority())
pq.print_queue()
