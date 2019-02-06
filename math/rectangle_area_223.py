"""
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
"""

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int -2
        :type B: int -2 
        :type C: int  2
        :type D: int  2
        :type E: int  3
        :type F: int  3
        :type G: int  4
        :type H: int  4
        :rtype: int
        """
        # idea: find intersection of two rectangles
        # x0, y0
        # x1, y1
        x0 = max(A,E)
        y0 = max(B,F)
        x1 = min(C,G)
        y1 = min(D,H)
        
        if x1<x0 or y1<y0:
            intersection_S = 0
        else:
            intersection_S = (x1-x0) * (y1-y0)
        S1 = (C-A)*(D-B)
        S2 = (G-E)*(H-F)
        return S1+S2-intersection_S