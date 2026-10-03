
class DupNums:
    def __init__(self, nums):
         self.nums = nums

    def find_duplicates(nums):
        result = []
        for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j]:
                        result.append(nums[i])
        unique = list(set(result))
        return unique;

nums = DupNums
unique = nums.find_duplicates([1,2,2,2,3])
print("unique num :",unique)
        
                   
    

    

