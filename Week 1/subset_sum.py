def subset_sum(nums, target):
    chosen = []
    def bt (i, total):
        if total == target:
            return list (chosen)
        if i == len(nums) or total > target:
            return None
        chosen.append (nums [i])
        hit = bt(i + 1, total + nums[i])
        if hit:
            return hit
        chosen.pop()
        return bt (i + 1, total)
    return bt (0, 0)
    
print(subset_sum([2, 3, 4, 8], 6))
