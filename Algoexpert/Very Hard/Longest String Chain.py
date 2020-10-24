# O(NM^2 + N log N) time | O(NM) space


def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextString": "", "maxChainLength": 1}

    sortedStrings = sorted(strings, key=len)
    for string in sortedStrings:
        findLongestStringChain(string, stringChains)
    return buildLongestStringChain(strings, stringChains)


def findLongestStringChain(string, stringChains):
    for i in range(len(string)):
        smallerString = getSmallerString(string, i)
        if smallerString not in stringChains:
            continue
        updateLongestStringChain(string, smallerString, stringChains)


def getSmallerString(string, index):
    return string[:index] + string[index + 1 :]


def updateLongestStringChain(currentString, smallerString, stringChains):
    smallerStringChainLength = stringChains[smallerString]["maxChainLength"]
    currentStringChainLength = stringChains[currentString]["maxChainLength"]
    if smallerStringChainLength + 1 > currentStringChainLength:
        stringChains[currentString]["maxChainLength"] = smallerStringChainLength + 1
        stringChains[currentString]["nextString"] = smallerString


def buildLongestStringChain(strings, stringChains):
    maxChainLength = 0
    chainStartingString = ""
    for string in strings:
        if stringChains[string]["maxChainLength"] > maxChainLength:
            maxChainLength = stringChains[string]["maxChainLength"]
            chainStartingString = string
    finalLongestStringChain = []
    currentString = chainStartingString
    while currentString != "":
        finalLongestStringChain.append(currentString)
        currentString = stringChains[currentString]["nextString"]
    return [] if len(finalLongestStringChain) == 1 else finalLongestStringChain
