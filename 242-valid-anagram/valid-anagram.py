class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s)!=len(t):
            return False
        CountS,CountT={},{}
        for i in range(len(t)):
            CountT[t[i]]=1+CountT.get(t[i],0)
            CountS[s[i]]=1+CountS.get(s[i],0)
        for c in CountT:
            if CountT[c]!=CountS.get(c,0):
                return False
        return True
        
            

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        