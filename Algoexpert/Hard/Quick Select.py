# O(N) time(average case) | O(N^2) time (worst case) | O(1) space

def quickSelect(array, k):
    return quickSelectHelper(array, 0, len(array) - 1, k-1)

def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            return
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while rightIdx >= leftIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx > position:
            endIdx = rightIdx - 1
        else:
            startIdx = rightIdx + 1
    

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
