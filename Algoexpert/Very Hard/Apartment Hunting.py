# O(NMN) time | O(N) space


def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
    return maxDistancesAtBlocks.index(min(maxDistancesAtBlocks))


def distanceBetween(i, j):
    return abs(i - j)


# O(NM) time | O(NM) space


def apartmentHunting(blocks, reqs):
    minDistancesFromBlock = list(map(lambda req: getMinDistance(blocks, reqs), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlock)
    return maxDistancesAtBlocks.index(min(maxDistancesAtBlocks))


def getMinDistance(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlock):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(
            map(lambda distances: distances[i], minDistancesFromBlock)
        )
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    return maxDistancesAtBlocks


def distanceBetween(i, j):
    return abs(i - j)
