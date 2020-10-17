# O(N) time | O(N) space


def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root, [])
    for i in range(len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNodes[0]


def getNodesInOrder(tree, array):
    if tree is not None:
        getNodesInOrder(tree.left, array)
        array.append(tree)
        getNodesInOrder(tree.right, array)
        return array


# O(N) time | O(d) space where d is depth of the tree


def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost


def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNode(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNode(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost

    return [leftMost, rightMost]


def connectNode(left, right):
    left.right = right
    right.left = left
