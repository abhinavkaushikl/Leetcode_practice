def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
        """
    n = len(digits)

    for i in range(n-1,-1,-1):
        if digits[i]<9:
           digits[i] += 1
           #print(digits[i])
           return digits
    
        digits[i] = 0
    #corner case
    return [1] + [0] * n
        
# Example usage:    
result = plusOne([2, 1, 9])
print(result)


# Example usage: