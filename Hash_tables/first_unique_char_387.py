"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        letter_positions = {}
        for i, ch in enumerate(s):
            if ch in letter_positions:
                letter_positions[ch] += [i]
            else:
                letter_positions[ch] = [i]
        result = [letter_positions[key][0] for key in letter_positions if len(letter_positions[key]) == 1]
        print(letter_positions)
        print(result)
        return -1 if result == [] else min(result)

solution = Solution()
solution.firstUniqChar("leetcode")
