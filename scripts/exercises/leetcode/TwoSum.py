# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, arr, target):
        for x in range(len(arr)):
            if (target - arr[x]) in arr:
                return arr.index(target - arr[x])

# class Solution:
#     def twoSum(self, arr, target):
        
#         memo = {}

#         for x in range(len(arr)):
#             if target - arr[x] in memo:
#                 return memo[target - arr[x]], x
#             else:
#                 memo[arr[x]] = x
                


# teste = Solution()
# print(teste.twoSum([2, 7, 11, 15], 9))