
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num # initalization
            length = 1
        while current_num + 1 in num_set:
            current_num +=1
            print(current_num)
            length +=1
        print('longest', longest)
        longest = max(longest, length)
    return longest
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive sequence length:", longestConsecutive(nums))
    # Output: Longest consecutive sequence length: 4