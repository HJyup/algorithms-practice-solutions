class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:
            if st and bracket in dic and dic[bracket] == st[-1]:
                st.pop()
            else:
                st.append(bracket)

        res = len(st) == 0
        print(st)
        return res