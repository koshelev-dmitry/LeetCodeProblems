class Solution(object):
    def reverseString(self, s):
        if s:
            # s = s[::-1]
            for i in range(len(s)//2):
                s[i], s[~i] = s[~i], s[i]
        