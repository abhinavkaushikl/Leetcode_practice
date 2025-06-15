def min_subarray_len(target, nums):
    left = 0 
    right =0
    total = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_length =  min(min_length,right-left+1)
            total -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0

# Example usage
min_length = min_subarray_len(7, [2,3,1,2,4,3])
print(min_length)  # Output: 2 (subarray [4,3] has length 2 and sum >= 7)