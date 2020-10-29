class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = maxSize
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    # O(1) time | O(1) space
    def insertKeyValuePair(self, key, value):
        if key is not self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    # O(1) time | O(1) space
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    # O(1) time | O(1) space
    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The key is not in cache!")
        self.cache[key].value = value

    def updateMostRecent(self, listNode):
        self.listOfMostRecent.setHeadTo(listNode)


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def removeBinding(self):
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head = node
            self.tail.previous = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBinding()
            self.head.previous = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.previous
        self.tail.next = None
