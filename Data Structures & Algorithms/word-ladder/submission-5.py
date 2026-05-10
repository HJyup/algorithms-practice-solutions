from collections import defaultdict, deque 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        encodings = defaultdict(set)
        visited_start = {beginWord: 1}
        visited_end = {endWord: 1}
        q_start = deque([beginWord])
        q_end = deque([endWord])

        for word in wordList:
            for i in range(0, len(word)):
                encodings[word[:i] + '*' + word[i+1:]].add(word)
        
        def bfsIteration(q, visited, visited_other):
            word = q.popleft()
            level = visited[word]
            for i in range(0, len(word)):
                encoding = word[:i] + '*' + word[i+1:]
                for curr_word in encodings[encoding]:
                    if curr_word in visited_other:
                        return level + visited_other[curr_word]
                    if curr_word not in visited:
                        visited[curr_word] = level + 1
                        q.append(curr_word)

        while q_start and q_end:
            if len(q_start) <= len(q_end):
                res = bfsIteration(q_start, visited_start, visited_end)
            else:
                res = bfsIteration(q_end, visited_end, visited_start)
            if res:
                return res
            
        return 0