class Solution:     
    def generateParenthesis(self, n: int) -> List[str]:
        #base case: length of string == 2n. Append and return if stack empty. Otherwise, just return
        #choices: "(" and append to stack. or ")" and pop from stack. 
                # Can choose ")" only if stack not empty. 
                # return if either leftps or rightps > n
        res = []
        string = []
        stack = []

        def backtrack(leftps, rightps):
            if len(string) == 2*n:
                if not stack:
                    res.append("".join(string.copy()))
                    return
                return
            if leftps > n or rightps > n:
                return
            
            string.append("(")
            stack.append("(")
            backtrack(leftps + 1, rightps)
            string.pop()
            stack.pop()

            if stack:
                string.append(")")
                temp = stack.pop()
                backtrack(leftps, rightps + 1)
                string.pop()
                stack.append(temp)

        backtrack(0, 0)
        return res



        
