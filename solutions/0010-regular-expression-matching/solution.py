class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p=r"^{}$".format(p)
        x=(re.compile(p)).finditer(s)
        for i in x:
            return True
        else:
            return False
