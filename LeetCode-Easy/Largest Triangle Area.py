# TIME - O(n**3)

def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def findArea(x1,y1,x2,y2,x3,y3):
            return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
        
        maxArea = 0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    ar = findArea(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1])
                    maxArea = max(maxArea,ar)
        return maxArea
