class Solution:
    def isValid(self, s: 'str') -> 'bool':
        brackets_map = {'(':')', '[':']', '{':'}'}
        brackets_to_close = []
        
        for c in s:
            if c in brackets_map:
                brackets_to_close.append(brackets_map[c])
            elif brackets_to_close != [] and c == brackets_to_close[-1]:
                brackets_to_close.pop()
            else:
                return False
            
        return brackets_to_close == []