class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,         2,         3,         4,         5,         6        ]
        #[2*3*4*5*6, 1*3*4*5*6, 1*2*4*5*6, 1*2*3*4*5, 1*2*3*4*6, 1*2*3*4*5]

        #[1,         1,       1*2,   1*2*3, 1*2*3*4, 1*2*3*4*5]
        #[2*3*4*5*6, 3*4*5*6, 4*5*6, 5*6,   6,       1]

        res = [1]
        for i in range(len(nums) - 1):
            res.append(res[-1] * nums[i])
        acc = 1
        for i in range(-1, -len(nums), -1):
            res[i - 1] = acc * nums[i] * res[i - 1]
            acc *= nums[i]

        return res
        