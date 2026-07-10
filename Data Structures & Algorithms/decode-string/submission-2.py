class Solution:
    def decodeString(self, s: str) -> str:
        #traverse string from left to right
        #if stack empty and not a number, add to res
        #if number, append (n, []) to stack and skip bracket
        #if closing bracket, pop, append to snd of new top, [] * n
        #if pop and then stack empty, append [] to res

        res = []
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "]":
                temp = stack.pop()
                substr = temp[1] * int("".join(temp[0]))
                if not stack:
                    res += substr
                else:
                    stack[-1][1] += substr
                i += 1
                continue
            if not stack and not s[i].isnumeric():
                res.append(s[i])
                i += 1
                continue
            if stack and not s[i].isnumeric():
                stack[-1][1].append(s[i])
                i += 1
                continue
            if s[i].isnumeric():
                num = []
                while s[i].isnumeric():
                    num.append(s[i])
                    i += 1
                i += 1 #skips bracket
                stack.append([num, []])
                continue
        
        return "".join(res)
            
            
            

            