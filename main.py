from typing import List
class Sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if (val + val2 == target and idx != idx2):
                    return [idx, idx2]

if __name__ == "__main__":
    s = input("Input: nums = ")
    target = int(input("target = "))
    s = s[1:-1]
    s = s.split(',')
    nums = list(map(int, s))
    i = Sum()
    print("Output: " + str(i.twoSum(nums, target)))
