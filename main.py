'''
Q1. what would the function return if no pair is found? 
A1. returns 0

Q2. 
'''

def pairs_with_given_sum(numbers,target):
    pairs = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)+1):
            if numbers[i] + numbers [j] == target:
                pairs += 1

    return pairs