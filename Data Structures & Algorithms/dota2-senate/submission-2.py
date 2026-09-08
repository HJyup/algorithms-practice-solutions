class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant, dire = 0, 0
        radiant_remove, dire_remove = 0, 0
        q = deque()

        for senator in senate:
            if senator == 'R':
                radiant += 1
            
            else:
                dire += 1

            q.append(senator)

        while q and radiant != 0 and dire != 0:
            senator = q.popleft()

            if senator == 'R' and radiant_remove > 0:
                radiant_remove -= 1

            elif senator == 'D' and dire_remove > 0:
                dire_remove -= 1

            else:
                if senator == 'R':
                    dire_remove += 1
                    dire -= 1

                else:
                    radiant -= 1
                    radiant_remove += 1
                
                q.append(senator)

        return 'Radiant' if radiant > 0 else 'Dire'