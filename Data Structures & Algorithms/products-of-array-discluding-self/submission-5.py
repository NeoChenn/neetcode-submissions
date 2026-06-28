class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 8, 48]
        #[48, 48, 24, 6], 
        prefixProduct = [nums[0]]
        postfixProduct = [nums[-1]]
        i, j = 1, len(nums) - 2
        while i < len(nums):
            prefixProduct.append(nums[i] * prefixProduct[-1])
            postfixProduct.append(nums[j] * postfixProduct[-1])
            i += 1
            j -= 1
        postfixProduct.reverse()
        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfixProduct[1]
            elif i == len(nums) - 1:
                nums[i] = prefixProduct[-2]
            else:
                nums[i] = prefixProduct[i - 1] * postfixProduct [i + 1]
        return nums