class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(1, len(nums)):
            pre.append(nums[i-1]*pre[-1])
        #print(pre)
        
        post = [1]
        for i in range(len(nums)-2, -1, -1):
            post.append(nums[i+1]*post[-1])
        post = post[::-1]
        #print(post)

        res = []
        for i in range(len(nums)):
            res.append(pre[i]*post[i])
        return res