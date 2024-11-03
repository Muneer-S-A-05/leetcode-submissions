class Solution(object):
    def reverse(self, x):
        if x>=0:
            x= int(str(x)[::-1])
        else:
            x= -int(str(x)[:0:-1])
        return 0 if (x>2147483648 or x<-2147483648) else x
