from pprint import pprint



class Solution:
    def twoSum(nums, target):
        hashMap = {} # val:index

        for i, n in enumerate(nums):       
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[nums[i]] = i
        return False #though it says that all test cases is guaranteed to return something, just adding it here for best practice
                
# array = [3,2,4]
# array = [3,3]
# target = 6
# array = [2,7,11,15]
# target = 9

# array = [2,4,11,3]
# target = 6
answer = Solution.twoSum(array,target)

print(answer)