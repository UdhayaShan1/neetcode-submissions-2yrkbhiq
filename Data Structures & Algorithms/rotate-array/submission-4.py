class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vis = {}
        
        for i in range(len(nums)):
            prev = nums[i]
            p = i
            #print('@', i)
            if i in vis:
                continue
            while True:
                nxt = (p+k)%len(nums)
                vis[p] = True
                
                tmp = nums[nxt]
                #print(p, nxt, prev, tmp, nums)
                nums[nxt] = prev
                prev = tmp
                p = nxt
                if nxt == i:
                    break

                




        