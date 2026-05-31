class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            # case 1. we just remove all elements that are smaller
            while st and st[-1] > 0 and a < 0 and abs(a) > st[-1]:
                st.pop()

            # case 2. if they are equal left
            if st and a < 0 and abs(a) == st[-1]:
                st.pop()
                continue

            # case 3. do not add element if it's smaller then prev
            if st and a < 0 and st[-1] > abs(a):
                continue

            st.append(a)

        return st