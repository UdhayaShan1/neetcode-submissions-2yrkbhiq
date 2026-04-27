class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        find = total//4
        arr = [0]*4
        matchsticks.sort(reverse=True)
        def back(k1, arr):
            if k1 >= len(matchsticks):
                for i in arr:
                    if i != find:
                        return False
                return True
            for i in range(len(arr)):
                if arr[i] + matchsticks[k1] > find:
                    continue
                arr[i] += matchsticks[k1]
                if back(k1+1, arr):
                    arr[i] -= matchsticks[k1]
                    return True
                arr[i] -= matchsticks[k1]

                # if arr[i] == 0:
                #     break
            return False
        return back(0, arr)