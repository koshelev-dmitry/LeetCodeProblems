class Solution:
    def isPalindrome(self, x):
        '''
        ## first variant
        if x < 0:
            return False
        res = []
        while x > 0:
            res.append(x % 10)
            x = x // 10
        return all([res[i] == res[~i] for i in range(len(res)//2)])
        ## variant two
        s = str(x)
        return s == s[::-1]
        ## variant three

        '''
        if x<0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        # 131
        while x > reverted_number: # 13 > 1
            reverted_number = reverted_number*10 + x % 10 # = 13
            x = x // 10 # 3
        return x == reverted_number or x == reverted_number//10