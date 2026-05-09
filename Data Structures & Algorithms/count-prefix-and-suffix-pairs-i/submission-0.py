class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ref1 = words[i]
                ref2 = words[j]
                ref1_r = ref1[::-1]
                ref2_r = ref2[::-1]
                #print(ref1_r, ref2_r)
                if ref2.startswith(ref1) and ref2_r.startswith(ref1_r):
                    res += 1
        return res
