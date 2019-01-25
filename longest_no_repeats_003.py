class Solution:
    def lengthOfLongestSubstring(self, s):
        longest_substr = 0
        substr = ''
        letter_positions = {}
        for i, letter in enumerate(s):
            if letter in letter_positions:
                longest_substr = max(longest_substr, len(substr))
                
                for j in range(letter_positions[substr[0]], letter_positions[letter]):
                    letter_positions.pop(s[j])
                
                substr = s[letter_positions[letter] + 1: i + 1]
                letter_positions[letter] = i

            else:
                letter_positions[letter] = i
                substr += letter
        return max(longest_substr, len(substr))

solution = Solution()
ln = solution.lengthOfLongestSubstring('dvdfv')
print(ln)