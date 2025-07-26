class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        test=nums
        how=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(test)):
                if j!=i and test[j]<nums[i]:
                   count+=1
            how.append(count)
        return how

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        