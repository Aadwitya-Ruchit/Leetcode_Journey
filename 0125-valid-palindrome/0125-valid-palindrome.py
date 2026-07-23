class Solution(object):
    def isPalindrome(self, s):
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        def check(i):
            if i>=len(clean)//2:
                return True
            if clean[i] != clean[len(clean)-i-1]:
                return False
            return check(i+1)
        return check(0)