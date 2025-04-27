'''
Q1. what would the function return if no pair sum is equal to target? 
A1. returns 0

Q2,what if the numbers list has no item?
A2. returns 0

Q3. what if the numbers list has only one item?
A3. returns 0

Q4. How will function handle the invalid input data type?
A4, function raise TypeError for invalid input.

Q5. How will function handle the invalid numbers list?
A5. It raise an Error with message "Please inter integer numbers"

Q6. does function counts duplicate pairs in the list?
A6. if pairs have different indices then Yes. (Exm. [3,3,3],6 => 3 pairs)

Q7. Does order of pairs matter?
A7. yes

Q8. does function accept negative integers as numbers or target?
A8. no

Q9. does function accepts 0?
A9. no for the target and yes for the list



'''
#  Time Complexity O(n^2)
#  Space Complexity O(n)

# def pairs_with_given_sum(numbers,target):
#     try:
#         # Validate input types
#         if not isinstance(target, int) or target < 0:
#             raise ValueError("Oops! Please enter the target as a non-negative integer.")
        
#         for num in numbers:
#             if not isinstance(num, int) or num < 0:
#                 raise ValueError(f"Invalid input in the list: {num}. All numbers must be positive integers.")
        
        
#         pairs = 0
#         unique_pairs = set()
#         for i in range(len(numbers)):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i] + numbers[j] == target and (numbers[i],numbers[j]) not in unique_pairs:
#                     unique_pairs.add((numbers[i],numbers[j]))
#                     pairs += 1

#         return pairs
    
#     except ValueError as e:
#         return str(e)

''' 
You can reduce the time complexity to O(n) by using a hash set (or dictionary) to track the numbers you’ve seen so far. 
This approach leverages the fact that lookups in a set (or dictionary) are on average O(1), 
making the algorithm much faster for large inputs.
'''
#  Time Complexity O(n)
#  Space Complexity O(n)

def pairs_with_given_sum(numbers, target):
    try:
        # Validate input types
        if not isinstance(target, int) or target <= 0:
            raise ValueError("Oops! Please enter the target as a non-negative integer.")
        
        for num in numbers:
            if not isinstance(num, int) or num < 0:
                raise ValueError(f"Invalid input in the list: {num}. All numbers must be positive integers.")
        
        pairs = 0
        seen_numbers = {} # changed from set() to Dict to include key/values
        
        for num in numbers:
            complement = target - num
            if complement in seen_numbers:
                # Count as many times as complement has occurred
                pairs += seen_numbers[complement]
            # Update how many times num has appeared
            seen_numbers[num] = seen_numbers.get(num, 0) + 1
        
        return pairs
    
    except ValueError as e:
        return str(e)


# print(pairs_with_given_sum(["1"],6)) 
# print(pairs_with_given_sum([1,5,1],6))
# print(pairs_with_given_sum([3,3,3,3],6))
# print(pairs_with_given_sum([6,3,0,3,6],6))
# print(pairs_with_given_sum([2,4,2,4],6))
print(pairs_with_given_sum([2,4,4,2],6))