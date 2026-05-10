class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        st = []

        for c in s:
            if c in hash_map:
                if st and st[-1] == hash_map[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return True if not st else False
        
        