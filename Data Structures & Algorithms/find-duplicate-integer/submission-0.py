class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Move a slow and fast pointer until they meet
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Start a second at the begginning of the input
        # Move both slow pointers until they meet
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
