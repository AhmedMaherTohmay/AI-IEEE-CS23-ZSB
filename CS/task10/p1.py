class Solution:
    def trap(self, height: List[int]) -> int:
        """
        left,right: pointers 
        maxleft and maxright: storing max left and max right to get the rain places
        ans : are the number where the rain is trapped 
        """

        left, right = 0, len(height)-1
        maxleft, maxright = 0, 0
        ans = 0
        while left < right:
            maxleft = max(maxleft, height[left])
            maxright = max(maxright, height[right])

            if maxleft < maxright:
                ans += maxleft-height[left]
                left += 1
            else:
                ans += maxright-height[right]
                right -= 1
        return ans


# 4 2 0 3 2 5
# 0 1 0 2 1 0 1 3 2 1 2 1
