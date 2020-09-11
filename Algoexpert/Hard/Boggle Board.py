# O(ws + nm.8^s) time |  O(ws + nm) space where s is the length of the largest word
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.addWord(word)
    visited = [[False for i in row] for row in board]
    finalWords = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(i, j, board, trie, visited, finalWords)

    return list(finalWords.keys())


def explore(i, j, board, trie, visited, finalWord):
    if visited[i][j]:
        return
    char = board[i][j]
    if char not in trie:
        return
    visited[i][j] = True
    trieNode = trie[char]
    if "*" in trieNode:
        finalWord[trieNode["*"]] = True
    list_of_neighbors = getNeighbors(i, j, board)
    for neighbor in list_of_neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWord)
    visited[i][j] = False


def getNeighbors(i, j, board):
    neighbors = []
    possibleDirections = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]
    for direction in possibleDirections:
        di, dj = direction
        newI, newJ = i + di, j + dj
        if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
            neighbors.append([newI, newJ])
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def addWord(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.endSymbol] = word
