class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        curr_max : temp int to store the maximum number 
        previous num: storing the previous number to compare it with the current max
        """
        curr_max = -1
        previous_num = -1
        for i in range(len(arr)-1, -1, -1):
            previous_num = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, previous_num)

        return arr
