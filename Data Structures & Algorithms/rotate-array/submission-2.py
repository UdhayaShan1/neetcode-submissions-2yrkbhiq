class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        vis = {}
        for i in range(len(nums)-k):
            carry = nums[i]
            curr = i
            while True:
                nxt = (curr+k)%len(nums)
                

                
                tmp = nums[curr]
                nums[curr] = carry
                carry = tmp
                curr = nxt
                if nxt in vis:
                    break
                vis[nxt] = True
                #print(curr, nxt, nums, carry)
        


            
        