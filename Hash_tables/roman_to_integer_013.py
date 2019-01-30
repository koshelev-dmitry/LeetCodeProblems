class Solution:
    def romanToInt(self, s):
        letter_to_arrabic = {
                'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1}
        number = 0
        for i in range(len(s)-1):
            num_cur = letter_to_arrabic[s[i]]
            num_next = letter_to_arrabic[s[i+1]]
            
            if num_cur < num_next:
                num_cur = -1*num_cur
            number += num_cur
            
        return number + letter_to_arrabic[s[-1]]

print(Solution().romanToInt('MCMXCIV'))