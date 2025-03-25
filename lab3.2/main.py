class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: TreeNode, depth=0) -> int:
    if root is None:
        return 0
    return depth + sum_of_depths(root.left, depth + 1) + sum_of_depths(root.right, depth + 1)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(sum_of_depths(root))
