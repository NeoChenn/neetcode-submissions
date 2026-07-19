class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #count num of opening and closing pars
        #can only add openPar when openPar <= n
        #can only add closePar when closePar < openPar

        res = []
        attempt = []

        def backtrack(openP, closeP):
            if (openP + closeP) == 2 * n:
                res.append("".join(attempt.copy()))
                return

            if openP < n:
                attempt.append("(")
                backtrack(openP + 1, closeP)
                attempt.pop()

            if closeP < openP:
                attempt.append(")")
                backtrack(openP, closeP + 1)
                attempt.pop()

        backtrack(0, 0)
        return res