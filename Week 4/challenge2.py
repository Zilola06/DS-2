def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i
    raise ValueError("No two sum solution exists")


assert two_sum([2, 7, 11, 15], 9) == (0, 1)
assert two_sum([3, 2, 4], 6) == (1, 2)
assert two_sum([-3, 4, 3, 90], 0) == (0, 2)
print("Challenge 2: all tests passed.")
