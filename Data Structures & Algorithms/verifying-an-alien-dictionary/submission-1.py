class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        for each word, compare with every other word
        O(n^2 * m * l) where n is the number of words, m is the length of order and l is the length of the longest word

        Compare words[i] with words[i - 1] for 1 <= i < len(words)
        O(n * m * l)

        to compare two words:
        store each letter in the hashmap, char : order
        compare character by character. until it differs.
        O(n * l)
        """
        if len(words) == 1:
            return True

        hashmap = {}
        for i, c in enumerate(order):
            hashmap[c] = i
        
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            length = min(len(w1), len(w2))
            isCorrect = False
            for j in range(length):
                if hashmap[w1[j]] > hashmap[w2[j]]:
                    return False
                elif hashmap[w1[j]] < hashmap[w2[j]]:
                    isCorrect = True
                    break
            if not isCorrect:
                if len(w1) > len(w2):
                    return False

        return True