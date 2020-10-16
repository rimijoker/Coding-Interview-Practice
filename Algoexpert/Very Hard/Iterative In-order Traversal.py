# O(N) time | O(1) space


class Node:
    """A binary tree node"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def morris_traversal(root):
    """Generator function for iterative inorder tree traversal"""

    current = root

    while current is not None:

        if current.left is None:
            yield current.data
            current = current.right
        else:

            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right

            if pre.right is None:

                # Make current as right child of its inorder predecessor
                pre.right = current
                current = current.left

            else:
                # Revert the changes made in the 'if' part to restore the
                # original tree. i.e., fix the right child of predecessor
                pre.right = None
                yield current.data
                current = current.right


# O(N) time | O(1) space


def inOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree
    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = (
                    currentNode.right
                    if currentNode.right is not None
                    else currentNode.parent
                )
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = (
                currentNode.right
                if currentNode.right is not None
                else currentNode.parent
            )
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode
