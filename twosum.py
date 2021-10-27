def twosum(nums : list, target : int) -> list:
    table = {} # key: num, value: index
    for i in range(len(nums)):# O(n)
        if nums[i] in table:# Check if nums[i] is in table
            return [table[nums[i]], i] # Return the index of the first number and the index of the second number
        table[target - nums[i]] = i # If not, add the number to the table
    return [] # If the number is not in the table, return an empty list



print(twosum([2,7,11,15], 9))
print(twosum([3,2,4], 6))
print(twosum([3,3], 6))
print(twosum([-1,0], -1))


