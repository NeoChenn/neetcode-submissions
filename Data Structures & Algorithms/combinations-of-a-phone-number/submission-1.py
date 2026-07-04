class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #hashmap key = digit, value = array of chars
        hashmap = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
        }
        #base case: len(comb) == len(digits)
        res = []
        combination = []
        def backtrack(index):
            if len(combination) == len(digits):
                res.append("".join(combination.copy()))
                return

            for c in hashmap[digits[index]]:
                combination.append(c)
                backtrack(index + 1)
                combination.pop()

        if not digits:
            return []
        backtrack(0)
        return res
            

            
