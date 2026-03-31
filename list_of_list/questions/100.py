# # 1. Sum Items in List

# # Write a Python program to sum all the items in a list.


# lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for i in range(0,len(lst)):
#     sum = sum + lst [i]
# print(sum)






# # 2. Multiply Items in List

# # Write a Python program to multiply all the items in a list.

# lst = [ 1, 2, 3, 4, 5]
# mul = 1
# for i in range(0,len(lst)):
#     mul = mul * lst [i]
# print(mul)






# # 3. Get Largest Number in List

# # Write a Python program to get the largest number from a list.


# lst = [ 1 ,2 ,3, 4, 5, 6, 7 , 10]
# max = lst[0]
# for i in range(0,len(lst)):
#     if max<lst[i]:
#         max = lst[i]
# print(max)





# # 4. Get Smallest Number in List

# # Click me to see the sample solutionProgramming


# lst = [-1 , 1 ,2 ,3, 4, 5, 6, 7 , 10]
# min = lst[0]
# for i in range(0,len(lst)):
#     if min>=lst[i]:
#         min = lst[i]
# print(min)







# # 5. Count Strings with Same Start and End

# # Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# # Sample List : ['abc', 'xyz', 'aba', '1221']
# # Expected Result : 2

# List = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for i in List:
#     if len(i) > 1 and i[0] == i[-1]:
#         count = count + 1
# print(count)






# # 6. Sort Tuples by Last Element

# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



# def last(n):
#     return n[-1]
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))





# # 7. Remove Duplicates from List
# # Write a Python program to remove duplicates from a list.

# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
# print(uniq_items)
# print(dup_items) 






# # 8. Check if List is Empty

# # Write a Python program to check if a list is empty or not.


# lst = []
# if len(lst) == 0:
#     print("Empty list")
# else:
#     print("non empty elements")









# # 9. Clone or Copy a List

# # Write a Python program to clone or copy a list.


# lst = [[1,2,3,4,5,10],[1,2,3]]
# new_lst = lst
# print(new_lst)



# # 10. Find Words Longer Than n

# # Write a Python program to find the list of words that are longer than n from a given list of words.



# str = "The quick brown fox jumps over the lazy dog"
# length = 3
# len_lst = []
# txt = str.split(" ")
# for i in txt:
#     if len(i) > length:
#         len_lst.append(i)
# print(len_lst)
    
        




# # 11. Check Common Member Between Two Lists

# # Write a Python function that takes two lists and returns True if they have at least one common member.

# # Define a function called 'common_data' that takes two lists, 'list1' and 'list2', as input
# def common_data(list1, list2):
#     result = False
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result

# print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9])) 





# # 12. Remove Specific Elements from List

# # Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# # Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # Expected Output : ['Green', 'White', 'Black']

# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# res1 = [ i for i in range(len(lst)) if i not in (0,4,5) ]
# res2 = [ x for (i , x)  in enumerate(lst)  if i not in (0,4,5) ]
# print(res1)
# print(res2)




# # 13. Generate 3D Array

# # Write a Python program to generate a 3*4*6 3D array whose each element is *.


# array = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
# print(array)
# array = []
# for i in range(3):          
#     layer = []
#     for j in range(4):      
#         row = []
#         for k in range(6):  
#             row.append("*")
#         layer.append(row)
#     array.append(layer)
# print(array)






# 14. Remove Even Numbers from List

# Write a Python program to print the numbers of a specified list after removing even numbers from it.

num = [7, 8, 120, 25, 44, 20, 27]
num = [x for x in num if x % 2 != 0]
print(num)





# # 15. Shuffle List

# # Write a Python program to shuffle and print a specified list.

# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)
 





# # 16. Generate Square Numbers in Range

# # Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).



# squares = []
# for i in range(1, 31):
#     if i*i:
#         squares.append(i*i)
# print("List:", squares)
# print("First 5 elements:", squares[:5])
# print("Last 5 elements:", squares[-5:])






# 17. Check If All Numbers Are Prime

# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.

# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False


def test(nums):
    return all(is_prime(i) for i in nums)

def is_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True





# 18. Generate All List Permutations

# Write a Python program to generate all permutations of a list in Python.








# 19. Calculate Difference Between Lists

# Write a Python program to calculate the difference between the two lists.
# Click me to see the sample solution

# 20. Access List Indices

# Write a Python program to access the index of a list.
# Click me to see the sample solution

# 21. Convert List to String

# Write a Python program to convert a list of characters into a string.
# Click me to see the sample solution

# 22. Find Index of List Item

# Write a Python program to find the index of an item in a specified list.
# Click me to see the sample solution

# 23. Flatten Shallow List

# Write a Python program to flatten a shallow list.
# Click me to see the sample solutionScripting language tools

# 24. Append One List to Another

# Write a Python program to append a list to the second list.
# Click me to see the sample solution

# 25. Select Random Item from List

# Write a Python program to select an item randomly from a list.
# Click me to see the sample solution

# 26. Check Circularly Identical Lists

# Write a Python program to check whether two lists are circularly identical.
# Click me to see the sample solution

# 27. Find Second Smallest Number in List

# Write a Python program to find the second smallest number in a list.
# Click me to see the sample solution

# 28. Find Second Largest Number in List

# Write a Python program to find the second largest number in a list.
# Click me to see the sample solution

# 29. Get Unique Values from List

# Write a Python program to get unique values from a list.
# Click me to see the sample solutionPython code snippets

# 30. Count Frequency of List Elements

# Write a Python program to get the frequency of elements in a list.
# Click me to see the sample solution

# 31. Count Elements in List Within Range

# Write a Python program to count the number of elements in a list within a specified range.
# Click me to see the sample solution

# 32. Check if List Contains Sublist

# Write a Python program to check whether a list contains a sublist.
# Click me to see the sample solution

# 33. Generate All Sublists

# Write a Python program to generate all sublists of a list.
# Click me to see the sample solution

# 34. Compute Primes Using Sieve of Eratosthenes

# Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
# Click me to see the sample solution

# 35. Create List with Range Concatenation

# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# Click me to see the sample solutionData structures algorithms

# 36. Get Variable ID or String

# Write a Python program to get a variable with an identification number or string.
# Click me to see the sample solution

# 37. Find Common Items in Lists

# Write a Python program to find common items in two lists.
# Click me to see the sample solution

# 38. Swap Every n-th and (n+1)th Values

# Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
# Click me to see the sample solution

# 39. Convert Integers List to Single Integer

# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
# Click me to see the sample solution

# 40. Split List by First Character

# Write a Python program to split a list based on the first character of a word.
# Click me to see the sample solution

# 41. Create Multiple Lists

# Write a Python program to create multiple lists.
# Click me to see the sample solution

# 42. Find Missing and Additional Values in Lists

# Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
# Click me to see the sample solution

# 43. Split List into Variables

# Write a Python program to split a list into different variables.
# Click me to see the sample solution

# 44. Generate Groups of Consecutive Numbers

# Write a Python program to generate groups of five consecutive numbers in a list.
# Click me to see the sample solution

# 45. Convert Pairs to Sorted Unique Array

# Write a Python program to convert a pair of values into a sorted unique array.
# Click me to see the sample solution

# 46. Select Odd Items from List

# Write a Python program to select the odd items from a list.
# Click me to see the sample solution

# 47. Insert Element Before Each List Item

# Write a Python program to insert an element before each element of a list.
# Click me to see the sample solution

# 48. Print Nested Lists

# Write a Python program to print nested lists (each list on a new line) using the print() function.
# Click me to see the sample solution

# 49. Convert List to List of Dictionaries

# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
# Click me to see the sample solution

# 50. Sort Nested Dictionaries in List

# Write a Python program to sort a list of nested dictionaries.
# Click me to see the sample solution

# 51. Split List Every Nth Element

# Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# Click me to see the sample solution

# 52. Difference Between Two Lists

# Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
# Click me to see the sample solution

# 53. Create List with Infinite Elements

# Write a Python program to create a list with infinite elements.
# Click me to see the sample solution

# 54. Concatenate List Elements

# Write a Python program to concatenate elements of a list.
# Click me to see the sample solution

# 55. Remove Key-Value Pairs from Dictionaries in List

# Write a Python program to remove key-value pairs from a list of dictionaries.
# Click me to see the sample solution

# 56. Convert String to List

# Write a Python program to convert a string to a list.
# Click me to see the sample solution

# 57. Check All Strings Match Given String

# Write a Python program to check if all items in a given list of strings are equal to a given string.
# Click me to see the sample solution

# 58. Replace Last Element with Another List

# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
# Click me to see the sample solution

# 59. Check if N-th Element Exists in List

# Write a Python program to check whether the n-th element exists in a given list.
# Click me to see the sample solution

# 60. Smallest Second Index Tuple

# Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# Click me to see the sample solution

# 61. Create List of Empty Dictionaries

# Write a Python program to create a list of empty dictionaries.
# Click me to see the sample solution

# 62. Print Space-Separated List Elements

# Write a Python program to print a list of space-separated elements.
# Click me to see the sample solution

# 63. Insert String Before List Items

# Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
# Click me to see the sample solution

# 64. Iterate Over Two Lists Simultaneously

# Write a Python program to iterate over two lists simultaneously.
# Click me to see the sample solution

# 65. Move Zeros to End of List

# Write a Python program to move all zero digits to the end of a given list of numbers.
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Click me to see the sample solution

# 66. Find List with Highest Sum

# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
# Click me to see the sample solution

# 67. Find Values Greater Than Specified Number

# Write a Python program to find all the values in a list that are greater than a specified number.
# Click me to see the sample solution

# 68. Extend List Without Append

# Write a Python program to extend a list without appending.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
# Click me to see the sample solution

# 69. Remove Duplicates from List of Lists

# Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]
# Click me to see the sample solution

# 70. Find Items Starting with Specific Character

# Write a Python program to find items starting with a specific character from a list.
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# []
# Click me to see the sample solution

# 71. Check If All Dictionaries Are Empty

# Write a Python program to check whether all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
# Click me to see the sample solution

# 72. Flatten Nested List Structure

# Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# Click me to see the sample solutionPython exercise solutions

# 73. Remove Consecutive Duplicates

# Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
# Click me to see the sample solution

# 74. Pack Consecutive Duplicates into Sublists

# Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
# Click me to see the sample solution

# 75. Create Run-Length Encoded List

# Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4.3, 5, 1]
# List reflecting the run-length encoding from the said list:
# [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# Original String:
# automatically
# List reflecting the run-length encoding from the said string:
# [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
# Click me to see the sample solutionAdvanced list techniques

# 76. Create Modified Run-Length Encoded List

# Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
# Click me to see the sample solution

# 77. Decode Run-Length Encoded List

# Write a Python program to decode a run-length message.
# Original encoded list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Decode a run-length encoded said list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Click me to see the sample solutionPython code snippets

# 78. Split List into Two Parts by Length

# Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])
# Click me to see the sample solution

# 79. Remove K-th Element from List

# Write a Python program to remove the K'th element from a given list, and print the updated list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]
# Click me to see the sample solution

# 80. Insert Element at Specified Position

# Write a Python program to insert an element at a specified position into a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]
# Click me to see the sample solutionPython exercise solutions

# 81. Extract Random Elements from List

# Write a Python program to extract a given number of randomly selected elements from a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]
# Click me to see the sample solution

# 82. Generate Combinations from List

# Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
# Click me to see the sample solution

# 83. Round Numbers and Calculate Total Sum

# Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243
# Click me to see the sample solutionAdvanced list techniques

# 84. Round Numbers, Find Min/Max, Multiply by 5

# Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110
# Click me to see the sample solution

# 85. Create Multidimensional List with Zeros

# Write a Python program to create a multidimensional list (lists of lists) with zeros.
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]
# Click me to see the sample solution

# 86. Create 3x3 Grid with Numbers

# Write a Python program to create a 3X3 grid with numbers.
# 3X3 grid with numbers:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# Click me to see the sample solutionPython code snippets

# 87. Sum Matrix Columns from Console Input

# Write a Python program to read a matrix from the console and print the sum for each column. As input from the user, accept matrix rows, columns, and elements separated by a space (each row).
# Input rows: 2
# Input columns: 2
# Input number of elements in a row (1, 2, 3):
# 1 2
# 3 4
# sum for each column:
# 4 6
# Click me to see the sample solution

# 88. Sum Primary Diagonal of Square Matrix

# Write a Python program to read a square matrix from the console and print the sum of the matrix's primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
# Input the size of the matrix: 3
# 2 3 4
# 4 5 6
# 3 4 7
# Sum of matrix primary diagonal:
# 14
# Click me to see the sample solutionPython exercise solutions

# 89. Zip Two Lists of Lists

# Write a Python program to Zip two given lists of lists.
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
# Click me to see the sample solution

# 90. Count Lists in Nested List

# Write a Python program to count the number of lists in a given list of lists.
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4
# Original list:
# [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# Number of lists in said list of lists:
# 3
# Click me to see the sample solution

# 91. Find List with Max and Min Lengths

# Write a Python program to find a list with maximum and minimum lengths.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (3, [3, 5, 7])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (4, [1, 34, 5, 7])
# List with minimum length of lists:
# (1, [12])
# Click me to see the sample solution

# 92. Check if Nested List Is Subset

# Write a Python program to check if a nested list is a subset of another nested list.
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# False
# Click me to see the sample solution

# 93. Count Sublists Containing Element

# Write a Python program to count the number of sublists that contain a particular element.
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
# [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:
# 3
# Count 'E' in the said list:
# 1
# Click me to see the sample solutionAdvanced list techniques

# 94. Count Unique Sublists in List

# Write a Python program to count the number of unique sublists within a given list.
# Original list:
# [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# Number of unique lists of the said list:
# {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# Original list:
# [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# Number of unique lists of the said list:
# {('green', 'orange'): 2, ('black',): 1, ('white',): 1}
# Click me to see the sample solution

# 95. Sort Strings in Sublists

# Write a Python program to sort each sublist of strings in a given list of lists.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
# Click me to see the sample solution

# 96. Sort List of Lists by Length and Value

# Write a Python program to sort a given list of lists by length and value.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
# Click me to see the sample solutionPython code snippets

# 97. Remove Sublists Outside Range

# Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contains an element outside the given range:
# [[13, 14, 15, 17]]
# Click me to see the sample solution

# 98. Scramble Letters in List Strings

# Write a Python program to scramble the letters of a string in a given list.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']
# Click me to see the sample solution

# 99. Find Max and Min in Heterogeneous List

# Write a Python program to find the maximum and minimum values in a given heterogeneous list.
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum and Minimum values in the said list:
# (5, 2)
# Click me to see the sample solutionPython exercise solutions

# 100. Extract Common Index Elements from Lists

# Write a Python program to extract common index elements from more than one given list.
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]
# Click me to see the sample solution
