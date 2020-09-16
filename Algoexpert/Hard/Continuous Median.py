# O(log N) time | O(1) space
# This question uses the concept of heaps


class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNCTION, [])
        self.greaters = Heap(MIN_HEAP_FUNCTION, [])
        self.median = None

    def insert(self, number):
        if len(self.lowers) == 0 or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalanceHeap()
        self.updateMedian()

    def rebalanceHeap(self):
        if len(self.lowers) - len(self.greaters) == 2:
            self.greaters.insert(self.lowers.remove())
        elif len(self.greaters) - len(self.lowers) == 2:
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self):
        if len(self.lowers) > len(self.greaters):
            self.median = self.lowers.peek()
        elif len(self.greaters) > len(self.lowers):
            self.median = self.greaters.peek()
        else:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, comparasionFunction, array):
        self.comparasionFunction = comparasionFunction
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent_index = (len(array) - 2) // 2
        for index in range(first_parent_index + 1):
            self.shiftDown(index, len(array) - 1, array)
        return array

    def shiftDown(self, currentIndex, lastIndex, heap):
        first_child_index = (2 * currentIndex) + 1
        while first_child_index <= lastIndex:
            second_child_index = (
                (2 * currentIndex) + 2 if (2 * currentIndex) + 2 <= lastIndex else -1
            )
            if second_child_index != -1 and self.comparasionFunction(
                heap[second_child_index], heap[first_child_index]
            ):
                index_to_swap = second_child_index
            else:
                index_to_swap = first_child_index
            if self.comparasionFunction(heap[index_to_swap], heap[currentIndex]):
                self.swap(index_to_swap, currentIndex, heap)
                currentIndex = index_to_swap
                first_child_index = (2 * currentIndex) + 1
            else:
                return

    def shiftUp(self, currentIndex, heap):
        parentIndex = (currentIndex - 2) // 2
        while currentIndex > 0 and self.comparasionFunction(
            heap[currentIndex], heap[parentIndex]
        ):
            self.swap(currentIndex, parentIndex, heap)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 2) // 2

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        removed_value = self.heap.pop()
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return removed_value


def MIN_HEAP_FUNCTION(a, b):
    return a < b


def MAX_HEAP_FUNCTION(a, b):
    return a > b
