# Write a function that takes an array of integers as input and returns the maximum difference between any two numbers in the array.
# Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

def max_difference(arr):

  if len(arr) < 2: #Make sure array is proper length
    return None

  min_num = float('inf') #Store the minumum and maximum number
  max_num = float('-inf')

  for num in arr: #O(n), Iterate through the array to find the minum and maximum number
    if num < min_num:
      min_num = num
    if num > max_num:
      max_num = num

  return max_num - min_num #Return the difference

""" Big O notation is O(n) the array gets passed once and the variables are extracted as directed to find the maximum range"""
# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_diff = max_difference(arr)
if max_diff is not None:
  print(f"The maximum difference between any two numbers in the array is: {max_diff}")
else:
  print("The array does not have a maximum difference.")
