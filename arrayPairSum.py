def arrayPairSum( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    sums = 0

    print(nums)
    if len(nums) < 2:
        return nums[0]

    if len(nums) == 2:
        return min(nums[0], nums[1])

    for i in range(0, len(nums) - 1, 2):
        print(i)

        j = i + 1
        sums += min(nums[i], nums[j])

    return sums

nums = [1,4,2,3]
print(arrayPairSum(nums))