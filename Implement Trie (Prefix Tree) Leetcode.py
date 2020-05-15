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
        trie['is_word'] = True

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