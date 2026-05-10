from collections import defaultdict, deque 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        encodings = defaultdict(set)
        count = 0
        visited = set()
        q = deque([beginWord])

        for word in wordList:
            for i in range(0, len(word)):
                encodings[word[:i] + '*' + word[i+1:]].add(word)

        while q:
            count += 1
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(0, len(word)):
                    encoding = word[:i] + '*' + word[i+1:]
                    for curr_word in encodings[encoding]:
                        if curr_word not in visited:
                            visited.add(curr_word)
                            q.append(curr_word)

        return 0

        
        