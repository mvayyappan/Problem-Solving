# # 1))

# # Given a list storing the names of employees as names = [‘Aanchal Sharma’, ‘Shubham Chhipa, ‘Mohit Rawat’, ‘Salman Khan’, ‘Ishani Janveja’]
# #    Given a list storing the dob of the employees as dob = [’24/03/1999′, ’19/08/1997′, ’07/07/1990′, ’26/11/2000′, ’14/10/1993′]
# #    Create a 3rd list storing their suggested passwords as per the following format:
# # Input: name = Aanchal Sharma
# #                dob = 24/03/1999
# # Output: pass = AS#03@24
# # Logic: Initials#MM@DD

# # names = ["Aanchal Sharma", "Shubham Chhipa" , "Mohit Rawat", "Salman Khan" , "Ishani Janveja"]
# # dob = ["24/03/1999" , "19/08/1997" , "07/07/1990" , "26/11/2000" , "14/10/1993"]



# name = "Aanchal Sharma"
# dob = "24/03/1999"
# parts = name.split()
# print(parts)
# first_initial = parts[0][0]
# last_initial = parts[1][0]
# dob_parts = dob.split("/")
# day = dob_parts[0]
# month = dob_parts[1]
# password = first_initial + last_initial + "#" + month + "@" + day
# print("pass =", password)















# # 2))

# # Create a list storing the number of vowels in the textual representation in the range of 0 to 9 in the following format,
# # [(0, 2), (1, 2), (2, 1)……]
# # Logic: 0 can be written as zero. zero has 2 vowels.


# # method 1:
# arr = [(0,"zero"),(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five"),(6,"six"),(7,"seven"),(8,"eight"),(9,"nine")]
# count = 0
# ar = []
# for i in range(len(arr)):
#     for j in range(len(arr[i][1])):
#         if arr[i][1][j] in "aeiou":
#             count = count + 1
#     ar.append((arr[i][0],count))
#     count = 0

# print(ar)












# # method 2:


# numbers = [
#     "zero", "one", "two", "three", "four",
#     "five", "six", "seven", "eight", "nine"
# ]

# vowels = "aeiou"
# result = []

# for i in range(10):
#     count = 0
#     for ch in numbers[i]:
#         if ch in vowels:
#             count += 1
#     result.append((i, count))

# print(result)














# # 3))

# # Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.
# #     Examples:  
# # Input : Bye Bye bro
# # Output : Bye bro
# # ——-
# # Input : Python is great and Java is also great
# # Output : is also Java Python and great



# txt = "Python is great and Java is also great"
# z = ""
# arr = []
# result = []
# for i in range(len(txt)):
#     if txt[i] == " ":
#         arr.append(z)
#         z = ""
#     else:
#         z = z + txt[i] 

# arr.append(z)

# for i in range(len(arr)):
#     if arr[i] not in result:
#         result.append(arr[i])

# for i in range(len(result)):
#     print(result[i],end=" ")













# # 4))

# # Write a Python program to count the number of elements in a list within a specified range.
# # Input: l = [2, 16, 9, 10, 15, 8, 11]
# # Input Range:
# #    Start: 9
# #    End:   13
# # Output:3


# arr = [2, 16, 9, 10, 15, 8, 11]
# Start = 9
# End = 13
# count = 0 

# for i in range(len(arr)):
#     if Start <= arr[i] <= End:
#         count = count + 1
# print(count)













# # 5))

# # l = ["Nimisha", "Harshil", "Naman", "Saurabh", "Manish"]
# # Output: [3, 2, 2, 3,2]



# l = ["Nimisha", "Harshil", "Naman", "Saurabh", "Manish"]
# arr =[]
# count = 0
# for i in range(len(l)):
#     count = 0
#     for j in range(len(l[i])):
#         if l[i][j] in "aeiou":
#             count = count + 1
#     arr.append(count)
# print(arr)














# # 6))


# # There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has. Create a list showing by what number(quantity) the candies needs to be redistributed so that all the kids have equal number of candies.
# # Input: candies = [2,3,6,1,3],
# # Output: [1, 0, -3, 2, 0]



# result = []
# arr = [ 2,3,6,1,3]
# sum = 0
# for i in range(len(arr)):
#     sum = sum + arr[i]
# avg = sum // len(arr)

# for i in range(len(arr)):
#     if arr[i] > avg:
#         result.append(avg-arr[i])
#     elif arr[i] < avg:
#         result.append(avg-arr[i])
#     else:
#         result.append(0)
        
# print(result)






# # 7))


# # Input: s = ‘How are you’
# # Output: so = ‘You are How’

# s = "How are you"
# arr = []
# txt = ""
# for i in range(len(s)):
#     if s[i] == " ":
#         arr.append(txt)
#         txt = ""
#     else:
#         txt = txt + s[i]

# arr.append(txt)

# for i in range(len(arr)-1,-1,-1):
#     print(arr[i],end=" ")







# # 8))

# # Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# # Example 1:
# # Input: nums = [1,2,3,4]
# # Output: [24,12,8,6]


# nums = [1,2,3,4]
# mul = 1
# result = []


# for i in range(len(nums)):
#     mul = 1
#     for j in range(len(nums)):
#         if nums[i] != nums[j]:
#             mul = mul * nums[j]
#     result.append(mul)
# print(result)








# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# Example 1:
# Input: s = “abc”, t = “ahbgdc”
# Output: True
# Example 2:
# Input: s = “axc”, t = “ahbgdc”
# Output: False





# s = "abc", 
# t = "ahbgdc"

# for i in range(len(s)):
#     if s[i] in t:
#         for j in range(len())




# # output:"cba fed"

# txt = ""
# arr = []

# a = "abc def"
# for i in range(len(a)):
#     if a[i] == " ":
#         arr.append(txt)
#         txt = ""
#     else:
#         txt = txt + a[i]
# arr.append(txt)
# for i in range(len(arr)):
#     for j in range(len(arr[i])-1,-1,-1):
#         print(arr[i][j],end="")
#     print(end = " ")




