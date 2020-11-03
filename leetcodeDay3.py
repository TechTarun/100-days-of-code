class Solution:
    def maxPower(self, s: str) -> int:
        max = 1
        ctr = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                ctr += 1
                if ctr > max:
                    max = ctr
            else:
                ctr = 1
        return max