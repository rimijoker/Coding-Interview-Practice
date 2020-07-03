class MinMaxStack(object):
    """Construct a with getMin() and getMax() with O(1) time complexity"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((x, x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1]), max(x, self.stack[-1][2])))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def getMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][2]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
