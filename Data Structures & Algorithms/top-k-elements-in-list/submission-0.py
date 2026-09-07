from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        cntr = Counter(nums)
        for key, val in cntr.items():
            buckets[val].append(key)
        topk = []
        for i in range(n, 0, -1):
            for el in buckets[i]:
                topk.append(el)
                if len(topk) == k:
                    return topk
        return topk