class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                res[stack[-1]] = i
                stack.pop()
            stack.append(i)
        #print(res)

        hmm = []
        pos = {}
        for i in range(len(nums2)):
            pos[nums2[i]] = i
        #@print(pos)
        for i in nums1:
            ans = -1 if res[pos[i]] == -1 else nums2[res[pos[i]]]
            hmm.append(ans)
        return hmm
