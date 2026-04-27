class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ref = []
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            ref.append(i)
        
        poss = {}
        for i in range(len(target)):
            poss[i] = False
        #print(poss)
        for i in ref:
            for j in range(len(i)):
                if i[j] == target[j]:
                    poss[j] = True
        for i in poss:
            if poss[i] == False:
                return False
        return True
            

            