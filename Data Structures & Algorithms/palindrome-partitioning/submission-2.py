class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # ----------------------------------------------------------------------------------------------
        # We cannot just prune on a fact that 'aaaab' is not palindrome because 'aaabaaa' can happen.
        # Therefore we need to check palindrom idea at the end.
        # But, we can prune on starting a new string (checking prev value for palindrome)
        # ----------------------------------------------------------------------------------------------
        res = []
        n = len(s)

        def isPalidrome(word: List[str]):
            left, right = 0, len(word) - 1

            while left <= right:
                if word[left] != word[right]:
                    return False

                left, right = left + 1, right - 1

            return True

        path = [[]]
        def dfs(i):
            nonlocal res

            if path and i == n and isPalidrome(path[-1]):
                arr = [arr[:] for arr in path]
                res.append([''.join(word) for word in arr])

            if i == n:
                return None

            # Include to current path
            path[-1].append(s[i])
            dfs(i + 1)
            path[-1].pop()

            # Finish this partition and go to next word
            if path[-1] and isPalidrome(path[-1]):
                path.append([s[i]])
                dfs(i + 1)
                path.pop()

            return None

        dfs(0)
        return res

        