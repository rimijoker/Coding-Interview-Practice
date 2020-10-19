# O(N) time | O(d) space where depth d = log N


def rightSiblingTree(root):
    mutate(root, None, None)
    return root


def mutate(node, parent, isLeftChild):
    if node is None:
        return
    leftNode = node.left
    rightNode = node.right
    mutate(leftNode, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(rightNode, node, False)
