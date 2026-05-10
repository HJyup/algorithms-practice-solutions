class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for st in strs:
            code = [0] * 26
            for a in st:
                code[ord(a) - ord('a')] += 1
            dct[tuple(code)].append(st)
            
        return list(dct.values())
        
        