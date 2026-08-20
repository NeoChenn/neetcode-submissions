class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def searchDfs(word, node):
            curr = node
            for i, c in enumerate(word):
                if c == ".":
                    for node in list(curr.children.values()):
                        if searchDfs(word[i + 1:], node):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.isEndOfWord
        return searchDfs(word, self.root)


