class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        g=""
        k=""
        for i in s:
            if i not in g:
                g+=i
            else:
                if len(g)>1:
                    g = g[g.index(i)+1::]+i
                else:
                    g = i
            if len(g)>len(k):
                k=g
        return len(k)
