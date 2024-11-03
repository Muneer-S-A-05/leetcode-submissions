class Solution(object):
    def convert(self, s, numRows):
        ans=""
        if numRows==1:
            return s
        m= (numRows-1)*2 #multiple
        for i in range(numRows):
            x=m-(i*2)
            j=i
            f=0
            while j<len(s):
                ans+=s[j]
                if x==0 or x==m:
                    j+=m
                    continue
                j+= x if f==0 else m-x
                f = 1 if f==0 else 0                    
        return ans
