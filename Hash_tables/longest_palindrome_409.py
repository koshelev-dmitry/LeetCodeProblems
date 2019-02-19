class Solution:
    def longestPalindrome(self, s: 'str') -> 'int':
        from collections import Counter
        count_of_letters = Counter(s)
        
        result = 0
        for key, val in count_of_letters.items():
            result += val // 2 * 2
            if result % 2 == 0 and val % 2 == 1:
                result += 1
            
        return result
            