class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            new.append(abs(i))
        chk = min(new)
        ind = 0
        for i in range(len(new)):
            if new[i] == chk:
                ind = i
                break
        #print(ind)
        left = ind-1
        right = ind+1

        res = [chk**2]
       # print(new)
        while left >= 0 and right < len(new):
            if new[left] <= new[right]:
                res.append(new[left]**2)
                left -= 1
            else:
                res.append(new[right]**2)
                right += 1
        #print(res)

        while left >= 0:
            res.append(new[left]**2)
            left -= 1
        while right < len(new):
            res.append(new[right]**2)
            right += 1
        return res

