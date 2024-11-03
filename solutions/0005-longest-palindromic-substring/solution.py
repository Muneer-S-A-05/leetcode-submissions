class Solution(object):
    def longestPalindrome(self, s):
        ans=""
        n=len(s)
        
        for i in range(n):

            l=r=i
            while l>-1 and r<n and s[l]==s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l-=1
                r+=1
            
            l=i
            r=i+1
            while l>-1 and r<n and s[l]==s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l-=1
                r+=1
        return ans
