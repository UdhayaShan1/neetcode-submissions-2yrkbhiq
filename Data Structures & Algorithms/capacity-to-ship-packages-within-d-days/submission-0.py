class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = 0
        end = sum(weights)
        res = end
        while start <= end:
            mid = (start+end)//2
            count = 0
            i = 0
            while i < len(weights):
                tmp = 0
                count += 1
                if weights[i] > mid:
                    count = float('inf')
                    break
                while i < len(weights) and tmp+weights[i] <= mid:
                    tmp += weights[i]
                    i += 1
            #print(count, "days", start, end)
            if count <= days:
                res = min(res, mid)
                end = mid-1
            else:
                start = mid+1
        return res
                
            
                
                
