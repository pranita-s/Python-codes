# TIME - O(n)

def minSwapsCouples(row):
        """
        :type row: List[int]
        :rtype: int
        """        
        person2pos = {}
        for i, r in enumerate(row):
            person2pos[r] = i       
        swaps = 0        
        for i in range(0,len(row),2):
            first, second = row[i:i+2]
            correctSecond = first - 1 if first % 2 else first + 1
            
            if second != correctSecond:
                correctSecondIndex = person2pos[correctSecond]
                row[i+1], row[correctSecondIndex] = row[correctSecondIndex], row[i+1]
                swaps += 1
                person2pos[correctSecond] = i+1
                person2pos[row[correctSecondIndex]] = correctSecondIndex
        
        return swaps
