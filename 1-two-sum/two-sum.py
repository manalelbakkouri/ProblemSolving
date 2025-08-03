class Solution(object):
    def twoSum(self, nums, target):
        
        hash_map={}
        
        for i , v in enumerate(nums):
            if target-v in hash_map :
               return [i , hash_map[target-v]]
            else :
               hash_map[v]=i

"""
hash_map is dict that stores v=difference of target and num in nums and i value of the v in the hashmap
for example = [2,11,7,15] t=9
hash_map :
v  i
2  0     9-2 =7 not in hash_map so we add it to hash_map
11 1
        9-7=2 , 2 in hash_map so we return i value of current eleement in the list which is 2 and hash_map[target-v] which is 0

"""