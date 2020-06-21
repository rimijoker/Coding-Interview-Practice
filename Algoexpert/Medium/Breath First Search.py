class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # step 1 > add root node to the queue, the node on which we are calling BFS
        queue = [self]
        while len(queue) > 0:
            # step 2 > pop the root/current node
            current = queue.pop(0)
            # step 3 > add the current node to the final array
            array.append(current.name)
            # step 4 > add the children of the current node to the queue
            for child in current.children:
                queue.append(child)
        return array
