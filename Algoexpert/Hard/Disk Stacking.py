# O(N^2) time | O(N) space


def diskStacking(disks):
    disks.sort(key=lambda disks: disks[2])
    heights = [disks[2] for height in disks]
    sequences = [None for value in disks]
    maxHeightIndex = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] > heights[maxHeightIndex]:
            maxHeightIndex = i
    return buildSequence(disks, heights, maxHeightIndex)


def areValidDimensions(other, current):
    return other[0] < current[0] and other[1] < current[1] and other[2] < current[2]


def buildSequence(array, sequences, currentIndex):
    sequence = []
    while currentIndex is not None:
        sequence.append(array[currentIndex])
        currentIndex = sequences[currentIndex]
    return list(reversed(sequence))
