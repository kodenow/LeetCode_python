from pprint import pprint



class Solution:
    def twoSum(nums, target):
            valCount = len(nums)
            maxGap = 0
            index = False
            array = list(nums)
            hashMap = {} # val:index
            # print(nums)
            # return False
            for i in range(0, valCount, 1):
                # pprint(i)
                # print(nums)
                diff = target - nums[i] #when you pop array.pop, you are also popping nums, the heck
                print('---------------------------------')
                print('diff ' + str(diff))
                print(hashMap)
                if diff in hashMap:
                    return [hashMap[diff],i]
                hashMap[nums[i]] = i
                # array.pop(0)
                
                # found = find in array
                # print(find)
                # print(found)
                # if found:
                #     if nums.index(find) > i:
                #         index = [i,nums.index(find)]
                #     else:
                #         index = [nums.index(find),i]

                #     return index
                
array = [3,2,4]
# array = [3,3]
target = 6
# array = [2,7,11,15]

# array = [2,4,11,3]
# target = 6
answer = Solution.twoSum(array,target)

print(answer)