class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        path_lst = list(filter(None, path.strip().split('/')))
        
        for token in path_lst:
            if token == '.':
                continue
            elif token == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(token)


        return '/' + '/'.join(ans)