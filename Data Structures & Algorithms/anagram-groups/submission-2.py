from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outer = defaultdict(list)
        for st in strs:
            d = defaultdict(int)
            for s in st:
                d[s] += 1
            outer[frozenset(d.items())].append(st)

        return list(outer.values())

        

            
                
        
        
        