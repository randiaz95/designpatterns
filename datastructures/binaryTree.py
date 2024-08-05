# EVERY NODE IS CAPABLE OF HOLDING A BINARY TREE WITHIN ITSELF
# THIS IS A SIMPLE EXAMPLE OF A BINARY TREE
# THE NODE CLASS IS CAPABLE OF HOLDING A LEFT AND RIGHT NODE
# THE NODE CLASS IS CAPABLE OF HOLDING A VALUE
# THE NODE CLASS IS CAPABLE OF HOLDING A BINARY TREE
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depthFirstSearch(node):
    if node is None:
        # You've reached the end of the tree the leaf has left or right thats empty.
        return

    print(node.value)
    depthFirstSearch(node.left)
    depthFirstSearch(node.right)

def depthFirstSearch(node):
    if node is None:
        # You've reached the end of the tree the leaf has left or right thats empty.
        return

    print(node.value)
    depthFirstSearch(node.left)
    depthFirstSearch(node.right)

def breadthFirstSearch(node):
    pass


if __name__ == "__main__":
    # Flip heads and tails
    # Probability of heads = 0.5

    # Create a binary tree
    justNode = Node(0.5)
    leftNode = Node(0.5)
    rightNode = Node(0.5)

    justNode.left = leftNode
    justNode.right = rightNode
