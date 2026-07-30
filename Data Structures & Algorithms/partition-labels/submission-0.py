class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        indecies = []

        for i, ch in enumerate(s):
            mp[ch] = i
        
        idx = 0
        for i in range(len(s)):
            idx = max(idx, mp[s[i]]) # if it's larget, we are going
            if idx == i:
                indecies.append(idx)

        ans = []
        for i in range(len(indecies)):
            if i > 0:
                ans.append(indecies[i] - indecies[i - 1])
            else:
                ans.append(indecies[i] + 1)

        return ans