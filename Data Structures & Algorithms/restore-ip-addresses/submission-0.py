class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        # place dot or not
        res = []

        address = []
        def backtrack(i: int) -> None:
            if i == n:
                if len(address) == 4:
                    res.append('.'.join(address))
                    
                return None

            if len(address) >= 4:
                return None

            for j in range(i, n):
                num = s[i : j + 1]
                if (len(num) > 1 and num[0] == '0') or int(num) > 255:
                    continue

                address.append(num)
                backtrack(j + 1)
                address.pop()

            return None

        backtrack(0)
        return res