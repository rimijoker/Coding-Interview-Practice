# O(NK) time | O(N + K) space where k is number of arrays


def mergeSortedArrays(arrays):
    sortedList = []
    elementIdxs = [0 for _ in arrays]
    while True:
        smallestItems = []
        for arrayIdx in range(len(arrays)):
            revelantArray = arrays[arrayIdx]
            elementIdx = elementIdxs[arrayIdx]
            if elementIdx == len(revelantArray):
                continue
            smallestItems.append(
                {"arrayIdx": arrayIdx, "num": revelantArray[elementIdx]}
            )
        if len(smallestItems) == 0:
            break
        nextItem = getMinValue(smallestItems)
        sortedList.append(nextItem["num"])
        elementIdxs[nextItem["arrayIdx"]] += 1
    return sortedList


def getMinValue(items):
    minValueIdx = 0
    for i in range(1, len(items)):
        if items[i]["nums"] < items[minValueIdx["nums"]]:
            minValueIdx = i
    return items[minValueIdx]


# O(N log K) time | O(N + K) space where k is number of arrays


def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIdx in arrays:
        smallestItems.append(
            {"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]}
        )
    minHeap = MinHeap(smallestItems)
    while not minHeap.isEmpty():
        smallestItem = minHeap.remove()
        elementIdx = smallestItems["elementIdx"]
        num = smallestItems["num"]
        arrayIdx = smallestItems["arrayIdx"]
        sortedList.append(num)
        if elementIdx == len(arrays[arrayIdx]) - 1:
            continue
        minHeap.insert(
            {
                "arrayIdx": arrayIdx,
                "elementIdx": elementIdx + 1,
                "num": arrays[arrayIdx][elementIdx + 1],
            }
        )
    return sortedList


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time | O(1) space
    def build_heap(self, array):
        first_parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent_index + 1)):
            self.shift_down(current_index, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def shift_down(self, current_index, end_index, heap):
        child_one_index = current_index * 2 + 1
        while child_one_index <= end_index:
            child_two_index = (
                current_index * 2 + 2 if current_index * 2 + 2 <= end_index else -1
            )
            if (
                child_two_index != -1
                and heap[child_two_index]["num"] < heap[child_one_index]["num"]
            ):
                index_to_swap = child_two_index
            else:
                index_to_swap = child_one_index
            if heap[index_to_swap]["num"] < heap[current_index]["num"]:
                self.swap(current_index, index_to_swap, heap)
                current_index = index_to_swap
                child_one_index = current_index * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def shift_up(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while (
            current_index > 0 and heap[current_index]["num"] < heap[parent_index]["num"]
        ):
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        # We mainly remove the root node by default. the first element of the array.
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        # Heap follows a stack data structure
        self.shift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
