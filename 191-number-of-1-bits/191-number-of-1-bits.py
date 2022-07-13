class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        input = list(str(bin(n)))
        for bits in input:
            if bits == '1':
                output += 1
        return output