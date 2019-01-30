class Solution:
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for i_a in range(len(A)):
            if A[i_a] == B[0]:
                i_b=0
                while i_b<len(B):
                    if A[(i_a + i_b) % len(A)] == B[i_b]:
                        i_b += 1
                    else:
                        break
                if i_b==len(B):
                    return True
        return False
                            
            
        '''
        Brute Force
        rotate = B
        for _ in range(len(A)): 
            if A == rotate:
                return True
            rotate = rotate[1:]+rotate[0]
        
        Fast Force
        return B in A+A
        '''
        