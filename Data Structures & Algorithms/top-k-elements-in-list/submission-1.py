class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = Counter(nums)

        # Convert dictionary into list of tuples
        # Example:
        # [(1, 3), (2, 2), (3, 1)]
        freq = list(count.items())

        # Sort by frequency in descending order
        # x[1] means the frequency value
        freq.sort(key=lambda x: x[1], reverse=True)

        result = []

        # Take the first k elements
        for i in range(k):
            result.append(freq[i][0])

        return result