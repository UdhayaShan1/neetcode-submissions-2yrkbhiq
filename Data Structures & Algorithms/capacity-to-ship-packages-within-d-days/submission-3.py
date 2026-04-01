class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #weights.sort()
        s = max(weights)
        e = sum(weights)

        def totalDays(w):
            d = 1
            i = 0
            curr = 0
            while i < len(weights):
                if curr + weights[i] <= w:
                    curr += weights[i] 
                else:
                    #print(d, curr)
                    d += 1
                    curr = weights[i]
                i += 1
            #print(d)
            return d <= days
        #print(totalDays(10))



        res = None
        while s <= e:
            mid = (s+e)//2
            if totalDays(mid):
                res = mid
                e = mid-1
            else:
                s = mid+1
        return res

            
