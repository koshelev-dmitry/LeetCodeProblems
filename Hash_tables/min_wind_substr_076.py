"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""
class Solution(object):
    def minWindow(self, s, t):
            from collections import Counter
            letters_to_cover = Counter(t)
            remaining_to_cover = len(t)
            left = 0
            result = s
            
            for right, letter in enumerate(s):
                if letter in letters_to_cover:
                    letters_to_cover[letter] -= 1
                    if letters_to_cover[letter] >= 0:
                        remaining_to_cover -= 1
                
                while remaining_to_cover == 0:
                    if right-left < len(result)-1:
                        result = s[left:right + 1]
                    
                    if s[left] in letters_to_cover:
                        letters_to_cover[s[left]] += 1
                        if letters_to_cover[s[left]] > 0:
                            remaining_to_cover += 1
                    left += 1
                    
            return "-" if left==0 else result

solution = Solution()
s = "ADOBECODEBAN"
t = "ABC"
print(solution.minWindow(s,t))