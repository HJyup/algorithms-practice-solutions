class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            while st and st[-1] > 0 and a < 0:
                if -a > st[-1]:
                    st.pop()
                elif abs(a) == st[-1]:
                    st.pop()
                    break
                else:
                    break
            else:
                st.append(a)

        return st