#fastest and correct solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #There is no built-in function to reverse a String in Python. https://www.w3schools.com/python/python_howto_reverse_string.asp 
        #https://stackoverflow.com/questions/509211/understanding-slicing
        #https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python ::-1
      
        return str(x) == str(x)[::-1] #we use slice <object_name>[<start_index>, <stop_index>, <step>]
                                     

sol = Solution()

answer = sol.isPalindrome(121)

print(answer)