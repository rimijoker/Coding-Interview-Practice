# O(N log N) time | O(d) space where d is depth


def allKindsOfNodeDepths(root):
    sumOfAllDepths = 0
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        sumOfAllDepths += nodeDepth(node)
        stack.append(node.left)
        stack.append(node.right)
    return sumOfAllDepths


def nodeDepth(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepth(node.left, depth + 1) + nodeDepth(node.right, depth + 1)


# O(N log N) time | O(d) space where d is depth


def allKindsOfNodeDepths(root):
    if root is None:
        return 0
    return (
        allKindsOfNodeDepths(root.left)
        + allKindsOfNodeDepths(root.right)
        + nodeDepth((root))
    )


def nodeDepth(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepth(node.left, depth + 1) + nodeDepth(node.right, depth + 1)


# O(N) time | O(N) space


def allKindsOfNodeDepths(root):
    nodeCounts = {}
    addNodeCount(root, nodeCounts)
    nodeDepths = {}
    addNodeDepths(root, nodeDepths, nodeCounts)
    return sumOfAllDepths(root, nodeDepths)


def sumOfAllDepths(node, nodeDepths):
    if node is None:
        return 0
    return (
        sumOfAllDepths(node.left, nodeDepths)
        + sumOfAllDepths(node.right, nodeDepths)
        + nodeDepths[node]
    )


def addNodeDepths(node, nodeDepths, nodeCounts):
    nodeDepths[node] = 0
    if node.left is not None:
        addNodeDepths(node.left, nodeDepths, nodeCounts)
        nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left]
    if node.right is not None:
        addNodeDepths(node.right, nodeDepths, nodeCounts)
        nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]


def addNodeCount(node, nodeCounts):
    nodeCounts[node] = 1
    if node.left is not None:
        addNodeCount(node.left, nodeCounts)
        nodeCounts[node] += nodeCounts[node.left]
    if node.right is not None:
        addNodeCount(node.right, nodeCounts)
        nodeCounts[node] += nodeCounts[node.right]
