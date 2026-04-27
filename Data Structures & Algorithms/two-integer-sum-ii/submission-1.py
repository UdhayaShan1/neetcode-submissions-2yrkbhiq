class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        chk = {}
        for i in range(len(numbers)):
            ref = numbers[i]
            if ref not in chk:
                chk[ref] = [float('inf'), -float('inf')]
            chk[ref][0] = min(i, chk[ref][0])
            chk[ref][1] = max(i, chk[ref][1])
        #print(chk)

        for i in range(len(numbers)):
            #print(i, numbers[i], target-numbers[i])
            if target-numbers[i] in chk and chk[target-numbers[i]][1] > i:
                return [i+1, chk[target-numbers[i]][1]+1]
        #return 