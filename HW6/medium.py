# Given an array of integers, write a function that finds the second largest number in the array.
# Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.



def find_second_largest(arr):

  if len(arr) < 2: #Make sure array is proper length
    return None

  largest = float('-inf') #Store the largest number, second largest number
  second_largest = float('-inf')

  for num in arr: #O(n), Iterate through array to evaluate the largest number, then use that to find the second highest number
    if num > largest:
      second_largest = largest
      largest = num
    elif num > second_largest and num != largest:
      second_largest = num

  if second_largest == float('-inf'):
    return None
  else:
    return second_largest

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_largest_num = find_second_largest(arr)
if second_largest_num is not None:
  print(f"The second largest number in the array is: {second_largest_num}")
else:
  print("The array does not have a second largest number.")

"""The Big-O notation would still be O(n) as the function needs to pass through the array once to 
evaluate the second largest number exemplified by the single for loop"""