class Solution:
    def wordBreak(self, s: str, w: List[str]) -> bool:
        return (f:=lambda i:[s[i:]]*(s[i:] in w)+[s[i:j]+' '+t for j in range(i+1,len(s)) if s[i:j] in w for t in f(j)])(0)