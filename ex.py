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

    def view_sorted_queue(self):
        sorted_list = []
        self._in_order_to_list(self.root, sorted_list)
        print("Відсортований список справ:")
        for item in sorted_list:
            print(f'{item[0]} (Пріоритет: {item[1]})')

    def _in_order_to_list(self, node, result):
        if node:
            self._in_order_to_list(node.left, result)
            result.append((node.value, node.priority))
            self._in_order_to_list(node.right, result)


def main():
    pq = PriorityQueue()
    while True:
        print("\n1: Додати справу")
        print("2: Переглянути чергу (відсортовано)")
        print("3: Видалити виконану справу")
        print("4: Завершити")
        choice = input("Оберіть дію: ")
        if choice == '1':
            value = input("Введіть назву справи: ")
            priority = int(input("Введіть пріоритет: "))
            pq.insert(value, priority)
        elif choice == '2':
            pq.view_sorted_queue()
        elif choice == '3':
            removed = pq.remove_highest_priority()
            if removed:
                print(f"Видалено справу з найвищим пріоритетом: {removed}")
            else:
                print("Черга порожня!")
        elif choice == '4':
            print("Завершення роботи.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")


main()
