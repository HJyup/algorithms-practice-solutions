class FreqStack:

    def __init__(self):
        # frequency - tracking value order for each frequency.
        # We need to track values per frequency for correct ordering

        # values - controlls max frequency for each value to correctly adding to freq
        self.frequency, self.values = {}, {}

        # shows current max freq for maping to frequency
        self.maxFrequency = 0

    def push(self, val: int) -> None:
        if val not in self.values:
            self.values[val] = 0

        self.values[val] += 1

        # create a new stack for a new tier of frequency
        if self.values[val] > self.maxFrequency:
            self.maxFrequency += 1
            self.frequency[self.maxFrequency] = []

        self.frequency[self.values[val]].append(val)
        return None

    def pop(self) -> int:
        val = self.frequency[self.maxFrequency].pop()
        self.values[val] -= 1
        
        if not self.frequency[self.maxFrequency]:
            self.maxFrequency -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()