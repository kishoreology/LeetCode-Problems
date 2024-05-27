class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n: int = len(nums)
        frequency: list[int] = [0 for _ in range(n + 1)]  # frequence[i] means there is frequence[i] elements equal to i

        for num in nums:
            frequency[min(n, num)] += 1

        num_greater_equal = 0
        for candidate_number in range(n, 0, -1):
            num_greater_equal += frequency[candidate_number]
            if candidate_number == num_greater_equal:
                return candidate_number

        return -1