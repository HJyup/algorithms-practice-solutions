class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1

        while i < len(chars):
            j = i
            count = 1

            while j < len(chars) and chars[j] == chars[i - 1]:
                chars[j] = '_'
                j += 1
                count += 1

            if count > 1:
                for ch in str(count):
                    chars[i] = int(ch)
                    i += 1

                i = j
            else:
                i += 1

        ptr = 0
        for i in range(len(chars)):
            if chars[i] != '_':
                chars[ptr] = str(chars[i])
                ptr += 1
        
        del chars[ptr:]
        return len(chars)