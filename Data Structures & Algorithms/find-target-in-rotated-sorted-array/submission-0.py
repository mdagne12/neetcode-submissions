class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left sorted side
            if nums[left] <= nums[mid]:
                # If smaller than the leftmost value in the window
                # then search right of the window
                if target < nums[left]:
                    left = mid + 1
                # If larger than mid then search right of the window
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # If larger than the rightmost value in the window, look left
                if target > nums[right]:
                    right = mid - 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

