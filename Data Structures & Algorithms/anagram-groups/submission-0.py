class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            li = [0 for _ in range(27)]
            for c in s:    
                li[ord(c)-97] += 1
            t = tuple(li)
            if t in anagrams:
                anagrams[t].append(s)
            else:
                anagrams[t] = [s]
        return list(anagrams.values())
