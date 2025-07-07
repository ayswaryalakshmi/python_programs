class Solution:
    def two_sum(self, num, target):
        seen = {}
        for i in range(len(num)):
            needed = target - num[i]
            if needed in seen:
                return [seen[needed], i]
            seen[num[i]] = i
