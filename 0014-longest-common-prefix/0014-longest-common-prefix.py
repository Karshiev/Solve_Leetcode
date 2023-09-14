class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        new_s = ""
        
        strs = sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return new_s
            new_s += first[i]
            
        return new_s 
        