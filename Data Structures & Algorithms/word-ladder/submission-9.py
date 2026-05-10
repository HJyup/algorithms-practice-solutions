class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def getCodes(word: str) -> List[str]:
            codes = []

            for i in range(len(word)):
                code = word[: i] + '*' + word[i + 1:]
                codes.append(code)

            return codes

        graph = collections.defaultdict(list)
        for word in wordList:
            codes = getCodes(word)

            for code in codes:
                graph[code].append(word)

        sequence = 0
        queue = collections.deque([beginWord])
        visited = set()

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                word = queue.popleft()
                if word == endWord:
                    return sequence + 1

                visited.add(word)
                codes = getCodes(word)

                for code in codes:
                    neighbours = graph[code]

                    for nei in neighbours:
                        if nei not in visited:
                            queue.append(nei)

            sequence += 1

        return 0