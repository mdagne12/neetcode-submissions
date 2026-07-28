class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1)

        while left <= right:
            # i + j represents the left partition
            # the left side should have ceil((m + n) / 2) elements
            i = (left + right) // 2 # middle index of nums1
            j = (len(nums1) + len(nums2) + 1) // 2 - i 

            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == len(nums1) else nums1[i]
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == len(nums2) else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                return float(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1
