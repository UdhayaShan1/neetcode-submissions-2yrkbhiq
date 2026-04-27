class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        indeg = {}
        for i in words:
            for j in i:
                indeg[j] = 0
                adjList[j] = {}

        
        def compare(str1, str2):
            i = 0
            j = 0
            while i < len(str1) and j < len(str2):
                if str1[i] != str2[j]:
                    seen = False if str2[j] not in adjList[str1[i]] else True
                    
                    adjList[str1[i]][str2[j]] = 1

                    if not seen:
                        indeg[str2[j]] += 1
                    return True
                i += 1
                j += 1
            return False
        #compare('z', 'o')
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if compare(words[i], words[j]):
                    continue
                if len(words[i]) > len(words[j]):
                    return ""
        #print(adjList, indeg)
        print(indeg)
        res = ""
        from queue import Queue
        q = Queue()
        for i in indeg:
            if indeg[i] == 0:
                q.put(i)
        while not q.empty():
            curr = q.get()
            res += curr
            if curr not in adjList:
                adjList[curr] = []
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.put(i)
        #print(res)
        return res if len(res) == len(indeg) else ""


            
            