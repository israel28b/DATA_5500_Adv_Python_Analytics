#Use Big-O notation to find the time complexity of the code you wrote. 
#Given an Array of integers, write a function to calculate the sum of all elements in the array


def sum_of_array(arr):
    sum = 0
    for num in arr:
        sum += num #O(n)
    return sum

array = [1,2,3,4,5,6,7,8,9,10]
array_sum = sum_of_array(array)

print("The sum of the array is: ", array_sum)

"""The Big O Notation would be O(n) because the function passes through the array a single time to find the sum, 
and it's processing time increases linearly with the more input added to the array"""