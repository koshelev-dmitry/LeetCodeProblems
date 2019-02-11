class Solution:
    def calculate(self, s: 'str') -> 'int':
        if s.strip() == "":
            return 0
        operators = {'+': lambda x,y: x+y,
                     '-': lambda x,y: x-y,
                     '*': lambda x,y: x*y,
                     '/': lambda x,y: x//y}
        i = 0
        nums_list = []
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                
                # if the previous operator is * or /
                prevous_operator = nums_list[-1] if len(nums_list) > 0 else ''
                if prevous_operator == '*' or prevous_operator == '/':
                    operatop = nums_list.pop()
                    previous_val = nums_list.pop()
                    nums_list.append(operators[prevous_operator](previous_val, num))
                else:
                    nums_list.append(num)
            elif s[i] in operators:
                nums_list.append(s[i])
                i += 1
            else:
                i += 1
        
        # open breakets, do summation
        if len(nums_list) > 1:
            result = int(nums_list[0])
            i = 1
            while i < len(nums_list):
                operator = nums_list[i]
                i += 1
                val = nums_list[i]
                i += 1
                result = operators[operator](result, val)
            return result
        else:
            return int(nums_list[0])
        
        
        
        
        