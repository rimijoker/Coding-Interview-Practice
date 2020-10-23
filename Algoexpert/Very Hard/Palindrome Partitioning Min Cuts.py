# O(N^3) time | O(N^2) space


def palindromePartitionMinCuts(string):
    palindromes = [[False for _ in string] for _ in string]
    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = isPalindrome(string[i : j + 1])
    cuts = [float("inf") for _ in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
    return cuts[-1]


def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


# O(N^2) time | O(N^2) space


def palindromePartitionMinCuts(string):
    palindromes = [[False for _ in string] for _ in string]
    for i in range(len(string)):
        palindromes[i][i] = True
    for length in range(2, len(string) + 1):
        for i in range(0, len(string) - length + 1):
            j = i + length - 1
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]
    cuts = [float("inf") for _ in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
    return cuts[-1]