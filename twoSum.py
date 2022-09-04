from pprint import pprint



class Solution:
    def twoSum(nums, target):
            valCount = len(nums)
            maxGap = 0
            index = False
            array = list(nums)
            hashMap = {} # val:index
 
            for i in range(0, valCount, 1):             
                diff = target - nums[i] #when you pop array.pop, you are also popping nums, the heck
                print(hashMap)
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