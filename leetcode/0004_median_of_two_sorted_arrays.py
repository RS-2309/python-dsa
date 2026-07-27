class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        low = 0
        high = len(nums1) - 1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            
            partition1 = (low + high)//2
            partition2 = half - partition1 - 1

            left1 = nums1[partition1] if partition1 >= 0 else float("-inf")

            right1 = nums1[partition1+1] if partition1 + 1 > len(nums1) else float("inf")

            left2 = nums2[partition2] if partition2 >= 0 else float("-inf")

            right2 = nums2[partition2+1] if partition2 + 1 > len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total%2 == 0:
                    return (max(left1, left2) + min(right1, right2))/2
                
                return min(right1, right2)
            
            elif left1 > right2:
                high = partition1 - 1

            else:
                low = partition1 + 1