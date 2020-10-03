# O(N) time | O(N) space
import collections


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        deque = collections.deque()
        for word in path.split("/"):
            if word not in [".", "..", ""]:
                deque.append(word)
            elif word == ".." and deque:
                deque.pop()
        return "/" + "/".join(deque)
