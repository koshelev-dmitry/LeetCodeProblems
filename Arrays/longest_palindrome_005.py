''' Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000. 
https://leetcode.com/problems/longest-palindromic-substring/

Solution took 884 seconds, faster than 81%.
Can be improved: using bubbles <- ->
'''

class Solution:
    def longestPalindrome(self, s):
        def ispalindrom(slice):
            for i in range(len(slice)//2):
                if slice[i]!=slice[~i]:
                    return False
            return True
        
        # if len(s) == 1:
        #     return s[0] 
        # if len(s) == 2 and s[0] == s[1]:
        #     return s
        
        longes_palindrom = ''
        window_size = 1 # size of the moving window 
        increaments = 0
        while window_size < len(s)+1:
            for i in range(len(s) - window_size + 1):
                # print(s[i:window_size + i])
                if ispalindrom(s[i:window_size + i]) and len(longes_palindrom) < window_size:
                    longes_palindrom = s[i:window_size+i]
                    increaments = 0
                    # print(f"Longest palindrome: {longes_palindrom}")
                    break
            window_size += 1
            increaments += 1
            if increaments == 3:
                return longes_palindrom
        return longes_palindrom

solution = Solution()
print(solution.longestPalindrome('cbbd'))