def find_duplicate(nums):
    """Faça o código aqui."""
    if (
        not nums
        or len(nums) < 2
        or not all(isinstance(item, int) for item in nums)
    ):
        return False

    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] < 0:
            return False

        if nums[i] == nums[i+1]:
            return nums[i]

    return False
    raise NotImplementedError
