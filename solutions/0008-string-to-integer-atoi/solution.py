class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = ""
        for i in s:
            if i==" " and k=="":
                continue
            elif i in "0123456789":
                k+=i
            elif i in "-+" and k=="":
                k=i
            else:
                break
        try:
            if int(k)<-2147483648:
                k=-2147483648
            elif int(k)>2147483647:
                k=2147483647
        except:
            k=0
        return int(k)
