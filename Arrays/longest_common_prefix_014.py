class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        index = 0
        prefix = ['']
        while True:
            for i in range(1, len(strs)):
                if len(strs[i]) > index and len(strs[i-1]) > index:
                    if strs[i][index] != strs[i-1][index]:
                        return ''.join(prefix)
                else:
                    return ''.join(prefix)
            try:
                prefix.append(strs[0][index])
            except:
                return ''.join(prefix)
            index += 1