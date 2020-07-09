"""
 The way we can build our Suffix-Trie is to use a bunch of hash tables or dictionaries. Where every node in the suffix
 tree is gonna be a Key in a dictionary, pointing to another dictionary/HashTable (the value of the key will store of
 the next node's dictionary directly so basically, it will be a nested dictionary of dictionary). And all the values in
 the dictionary, will be the other nodes in the tree whose keys will be a specific letter that comes after the previous
 letter, and that points to another hash table, and so on and so forth.
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.tries
        for character in word:
            if character not in trie:
                trie[character] = {}
            trie = trie[character]
        trie["is_word"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.tries
        for character in word:
            if character not in trie:
                return False
            trie = trie[character]
        return "is_word" in trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.tries
        for character in prefix:
            if character not in trie:
                return False
            trie = trie[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
