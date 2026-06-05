class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower().strip()
        i = 0
        j = len(s)-1
        while i < j:
            if not ((ord(st[i]) >= ord("0") and ord(st[i]) <= ord("9")) or (ord(st[i]) >= ord("a") and ord(st[i]) <= ord("z"))):
                i += 1
                continue
            if not ((ord(st[j]) >= ord("0") and ord(st[j]) <= ord("9")) or (ord(st[j]) >= ord("a") and ord(st[j]) <= ord("z"))):
                j -= 1
                continue
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True