class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def diff(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    return (word1[i], word2[i])
            return None
        #print(diff("hrn", "hrf"))

        adjList = {}
        indeg = {}
        out = {}
        for i in range(len(words)):
            for j in words[i]:
                adjList[j] = []
                indeg[j] = 0 
                out[j] = 0


        for i in range(len(words)):
            for j in range(i+1, len(words)):
                diff_char = diff(words[i], words[j])
                if not diff_char:
                    if len(words[i]) > len(words[j]):
                        return ""
                    continue
                #print(words[i], words[j], diff_char)

                adjList[diff_char[0]].append(diff_char[1])
                indeg[diff_char[1]] += 1
                out[diff_char[0]] += 1
        #print(adjList, indeg, out)

        vis = {}
        parent = {}
        def cycle(node):

            vis[node] = 1
            parent[node] = 1
            for i in adjList[node]:
                if i not in vis:
                    if cycle(i):
                        return True
                elif i in parent:
                    if i in parent:
                        return True
            del parent[node]
            return False
        for i in adjList:
            if cycle(i):
                return ""




        from queue import Queue
        q = Queue()
        for i in indeg:
            if indeg[i] == 0:
                q.put(i)
        res = ""
        while not q.empty():
            curr = q.get()
            res += curr
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.put(i)
        #print(res)
        return res


                

        