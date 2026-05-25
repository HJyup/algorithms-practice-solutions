class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        ptr = 1

        while i < len(chars):
            if chars[i] == chars[i - 1]:
                j = i
                count = 1

                while j < len(chars) and chars[j] == chars[i - 1]:
                    j += 1
                    count += 1   

                for ch in str(count):
                    chars[ptr] = int(ch)
                    ptr += 1

                i = j                    
            else:
                chars[ptr] = chars[i]
                i += 1
                ptr += 1
        
        del chars[ptr:]
        return len(chars)