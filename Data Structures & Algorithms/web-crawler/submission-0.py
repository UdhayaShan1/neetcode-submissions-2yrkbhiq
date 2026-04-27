# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        #print(htmlParser.getUrls(startUrl))

        def sameHost(url1, url2):
            url1 = url1.split("//")[1].split('/')[0]
            url2 = url2.split('//')[1].split('/')[0]
            #print(url1, url2)
            return url1 == url2

        vis = {}
        def dfs(node):
            vis[node] = True
            urls = htmlParser.getUrls(node)
            #print(node, urls)
            for i in urls:
                if i in vis or not sameHost(node, i):
                    continue
                dfs(i)
        dfs(startUrl)
        return list(vis.keys())
            
        