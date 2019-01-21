class Solution(object):

    # My first solution
    def _findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        
        import collections
        dic_p = collections.defaultdict(int)
        for letter in p:
            dic_p[letter] = dic_p[letter] + 1
        
        result = []
        # initialize sliding dictionary of length p
        sliding_dict = collections.defaultdict(int)
        for i in range(len(p)):
            sliding_dict[s[i]] = sliding_dict[s[i]] + 1
        if dic_p == sliding_dict:
            result.append(0)
        
        for i in range(len(s) - len(p)):
            sliding_dict[s[i]] = sliding_dict[s[i]] - 1 # Remove the element
            if sliding_dict[s[i]] == 0:
                del sliding_dict[s[i]]
            # Add new element:
            sliding_dict[s[i+len(p)]] = sliding_dict[s[i+len(p)]] + 1 # Remove the element
            if dic_p == sliding_dict:
                result.append(i+1)
        return result

solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))