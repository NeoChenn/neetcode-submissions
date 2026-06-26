class Solution:
    def isValid(self, s: str) -> bool:
        #stack. If a close bracket, most recently opened must be the same type.
        #True if stack is empty at the end of the string
        
        myMap = {
                    ')' : '(',
                    ']' : '[',
                    '}' : '{'
                }

        stack = []
        openings = list(myMap.values())
        for br in s:
            if br in openings:
                stack.append(br)
            else:
                if not stack or myMap[br] != stack[-1]:
                    return False
                stack.pop()
        if stack:
            return False
        return True
                