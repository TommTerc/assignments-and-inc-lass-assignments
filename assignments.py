def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            result = [seen[complement], i]
            print(f"Indices: {result}")
            return result
        seen[num] = i
    return []

# Example usage
nums = [2,7,11,15]
target = 9
twoSum(nums, target)