class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range (len(nums))]
        postfix = [1 for i in range (len(nums))]
        prefixProduct = 1
        suffixProduct = 1
        for i in range(len(nums)):
            prefixProduct *= nums[i]
            prefix[i] = prefixProduct
        for i in range(len(nums)-1, -1, -1):
            suffixProduct *= nums[i]
            postfix[i] = suffixProduct
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i+1])
            elif i == (len(nums)-1):
                output.append(prefix[i-1])
            else:
                output.append(postfix[i+1]*prefix[i-1])
        return output