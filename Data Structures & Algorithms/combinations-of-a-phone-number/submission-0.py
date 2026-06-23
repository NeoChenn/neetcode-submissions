class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #[def, ghi, jkl]

        digitToLetters = {
                    "2" : "abc", 
                    "3" : "def",
                    "4" : "ghi", 
                    "5" : "jkl", 
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"
                    }

        if digits == "":
            return []
            
        digits = list(digits)
        for i in range(len(digits)):
            digits[i] = digitToLetters[digits[i]]

        res = []
        combination = []
        def backtrack(i):
            if len(combination) == len(digits):
                res.append("".join(combination.copy()))
                return
            
            for letter in digits[i]:
                combination.append(letter)
                backtrack(i + 1)
                combination.pop()

        backtrack(0)
        return res