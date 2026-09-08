from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        result = []
        for num, count in counted.most_common(k):
            result.append(num)
        return result