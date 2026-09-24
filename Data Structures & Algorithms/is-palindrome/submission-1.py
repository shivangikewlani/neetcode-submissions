class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s:
            if c.isalnum():
                s1+=c.lower()
        l =0 
        r= len(s1)-1
        #print(s1)
        while l <= r:
            #print(s1[l], " ", s1[r])
            if s1[l]!=s1[r]:
                #print(l, "gh", r, s1[1], " hjh", s1[r])
                return False
            l+=1
            r-=1
        return True
        