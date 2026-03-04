# # 1)


# # You are provided with a number 'n'. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits. You are given with a number n.  Print 'Saturated' if it is saturated else it is 'Unsaturated'.
# # Bonus: Don’t use `String() and split()` inside the input and use 
# # Example:  Input: 121, Output:  Saturated
# # Explanation: The number is made up of only two digits i.e. 1 and 2


# def saturated(n):
#     res = []
#     while n>0:
#         digit = n%10
#         if digit not in res:
#             res.append(digit)
#         n = n//10
        
#     if len(res) == 2:
#         print("Saturated")
#     else:
#         print("UnSaturated")

# saturated(1)
# saturated(12)
# saturated(123)






# # 2)

# # Second Maximum Number

# def sec_max(arr):
#     max = arr[0]
#     sec_max = arr[0]
#     for i in range(0,len(arr),+1):
#         if arr[i]>max:
#             max=arr[i]
#     for j in range(0,len(arr),+1):
#         if arr[j]>sec_max and max!=arr[j]:
#             sec_max=arr[j]
#     print(sec_max)


# sec_max([12,34,56,78,90,1,2,9])






# # 3)



# # Given a list of N integers(nums), return all integers (in a list) which are divisible by the previous integer.



# def prev_device(arr):
#     res = []
#     for i in range(1,len(arr),+1):
#         if arr[i]%arr[i-1]==0:
#             res.append(arr[i])
#     print(res)



# prev_device([1,2,3,6,7])








# # 4)


# # You are given a string and you need to remove all the repeating characters inside it.
# # Example:
# # Input: “mississipie”
# # Output: “mpe”



# def remove_repeat(s):
#     count = 0
#     res = ""
#     for i in range(0,len(s)):
#         count  = 0
#         for j in range(0,len(s)):
#             if s[i] == s[j]:
#                 count = count + 1
#         if count == 1:
#             res = res + s[i]
#     print(res)

# remove_repeat("mississipie")








# # 5)

# # You are given with an circular array .Your task is calculate the difference between two consecutive number.
# #  And if absolute difference is greater than 'k', print 1 else print 0

# def array_diff(arr,k):
#     res = []
#     for i in range(0,len(arr)):
#         diff = arr[i] - arr[(i+1)%len(arr)]
#         if diff<0:
#             diff = -diff
#         if diff > k:
#             res.append(1)
#         else:
#             res.append(0)
#     print(res)

# array_diff([50,65,85,98,35],15)








# # 6)


# #  all numbers is divisible by 2, 3 and 5.  Print 1 if array is beautiful and 0 if it is not

# def beautiful(arr):
#     sum = 0
#     for i in range(0,len(arr)):
#         sum = sum + arr[i]
#     if sum%2==0 and sum%3==0 and sum%5==0:
#         print(1)
#     else:
#         print(0)
    
    
# beautiful([5, 25, 35, -5, 30])








# # 7)


# # Find the Single Occurring Number


# def distinct(arr):
#     dict = {}
#     for i in range(0,len(arr)):
#         if arr[i] not in dict:
#             dict[arr[i]] = 1
#         else:
#             dict[arr[i]] = dict[arr[i]] + 1
#     for key in dict:
#         if dict[key] == 1:
#             print(key)


# distinct([1,2,3,4,5,6,5,4,3,2,1])






# # 8)


# # Strings Digits Sum

# def str_sum(s):
#     sum = 0
#     num = "1234567890"
#     for i in range(0,len(s),+1):
#         if s[i] in num:
#             sum = sum + int(s[i])
#     print(sum)
# str_sum("ikjreh873q6ydjnb")





# # 9)

# # Sum of Square of Numbers

# def sum_square(n):
#     sum = 0
#     while n>0:
#         digit  = n%10
#         digit = digit**2
#         sum = sum + digit 
#         n = n // 10
#     print(sum)
# sum_square(129)








# # 10)

# # First Non-Repeating Character in a String

# def first_distinct(s):
#     dict = {}
#     if len(s) == 0:
#         print("None")
#     else:
#         for i in range(0,len(s)):
#             if s[i] not in dict:
#                 dict[s[i]] = 1
#             else:
#                 dict[s[i]] = dict[s[i]] + 1
#         for key in dict:
#             if dict[key] == 1:
#                 print(key)
#                 break
#             else:
#                 print("none")
# first_distinct("aabbcde")








# # 11)

# # A number is called a Strong Number if the sum of factorials of its digits equals the number itself.

# def strong(n):
#     a = n
#     fact = 1
#     sum = 0
#     while n>0: 
#         fact = 1
#         digit = n%10
#         for i in range(1,digit+1):
#             fact = fact * i
#         sum = sum + fact
#         n = n // 10
#     if a == sum:
#         print("Strong")
#     else:
#         print("Not Strong")
# strong(145)









# # 12)

# # Move All Zeros to End


# from http.client import RANGE_NOT_SATISFIABLE


# def move_zeros(arr):
#     res = []
#     count = 0
#     for i in range(0,len(arr),+1):
#         if arr[i] == 0:
#             count = count + 1
#         else:
#             res.append(arr[i])
#     for j in range(1,count+1):
#         res.append(0)
#     print(res)
# move_zeros([1,2,3,4,5,0,0,0,0,2,3,5])







# # 13)

# # You are given a list containing numbers from 1 to n, but one number is missing.
# #  Find the missing number.


# def find_miss_num(arr):
#     max = arr[0]
#     sum = 0
#     for i in range(0,len(arr)):
#         sum = sum + arr[i]
#         if arr[i]>max:
#             max = arr[i]
#     find = max * (max+1)//2
#     diff = find - sum 
#     print(diff)
# find_miss_num([1,2,3,5,6,7])








# # 14)

# # Find the Largest Odd Number in a List

# from gettext import find


# def find_large_odd(arr):
#     if len(arr) == 0:
#         print("invalid")
#     elif len(arr) == 1:
#         if arr[0]%2==0:
#             print("No odd number")
#         else:
#             print(arr[0])
#     else:
#         max = arr[0]
#         for i in range(0,len(arr)):
#             if arr[i]%2==1:
#                 if arr[i]>max:
#                     max = arr[i]
#         print(max)
# find_large_odd([9,1,2,3,5])










# # 15)

# # Your task is to calculate net goal rate of each team. Net goal rate of team 
# # is calculated as No of goals(team[i])- sum of(no of goals by last 3 teams).
# # Input: [95,85,75,12,11], Output: [-3,-13,-23,-86,-87]


# def different_team(arr):
#     res = [] 
#     sum = arr[-1] + arr[-2] + arr[-3]
#     for i in range(0,len(arr),+1):
#         res.append(arr[i]-sum)
#     print(res)
# different_team([95,85,75,12,11])
        







# # 16)


# # You are given a list of “n” numbers . The list is imposed with a condition all the elements are in range from zero to n-1. 
# # Your tasks is to rearrange the elements from nums[i] = nums[num[i]]


# def rearrangement(arr):
#     if len(arr) == 0:
#         print("invalid")
#     elif len(arr) == 1:
#         print(arr[0])
#     else:
#         array = []
#         for i in range(len(arr)):
#             array.append(arr[arr[i]])
#         print(array)
# rearrangement([4,0,2,1,3])
# rearrangement([1])
# rearrangement([2,0,1,4,5,3])










# # 17)

# # n = 4
# # * 
# # * * *
# # * * * * *
# # * * * * * * * 


# def patterns(n):
#     for i in range(1,n+1):
#         for j in range(i*2-1):
#             print("*",end=" ")
#         print()
# patterns(4)






# # 18)

# # n = 5
# # *
# # **
# # ***
# # ****
# # *****

# def patterns(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print()
# patterns(5)
# patterns(6)







# # 19)

# # Given a string count number of distinct vowels in the String. Consider all the inputs to be in lowercase
# # Input: cool
# # Output: 1
# # Explanation: Since o is coming twice, but we need distinct counts so its only 1.



# def count_vowel(s):
#     res = ""
#     count = 0
#     for i in range(0,len(s),+1):
#         if s[i] not in res:
#             res = res+s[i]
#     for i in range(0,len(res),+1):
#         if res[i] in "aeiou":
#             count = count + 1
#     print(count)


# count_vowel("coooooooolu")








# # 20)

# # A company records the energy output (in kWh) from a solar panel for 15 days.
# # An “efficiency drop streak” occurs when three consecutive days show decreasing output. Given the list, determine how many such streaks occur.
# # Example: Input : [50, 48, 45, 49, 47, 46, 44], Output: 2
# # Explanation: (Streaks: 50→48→45 and 49→47→46)
# # So the count becomes 2


# def KWH(arr):
#     count = 0
#     for i in range(2,len(arr)):
#         if arr[i] < arr[i-1] < arr[i-2]:
#             count = count + 1
#     print(count)
# KWH([50, 48, 45, 49, 47, 46, 44])








# # 21)


# # Count which word has more ‘a’


# def count_a(arr):
#     max_count = 0 
#     max_word = ""
#     for i in range(0,len(arr)):
#         count = 0
#         for j in range(0,len(arr[i])):
#             if arr[i][j] == "a":
#                 count = count + 1 
#         if count > max_count:
#             max_count = count
#             max_word = arr[i]
#     print(max_word) 
# count_a(["apple", "appeal", "after", "banish"])










# # 22)

# # Count Words Ending with a Vowel
# #   Write a function `count_vowels(sentence)`to count how many words in a sentence end with a vowel.
# #   (Bonus: Do not use `split()` — handle manually using loops) 
# # Example:
# # Input: sentence = "I like to code everyday", Output: 4 
# # Explanation: There are four words - I, like, to, code




# def count_vowels(s):
#     txt = ""
#     arr = []
#     for i in range(0,len(s)):
#         if s[i] == " ":
#             arr.append(txt)
#             txt = ""
#         else:
#             txt = txt + s[i]
#     arr.append(txt)
#     res = []
#     for i in range(len(arr)):
#         if arr[i][-1] in "aeiouAEIOU":
#             res.append(arr[i])
#     print(res)
                
# count_vowels("I like to code everyday")
        








# # 23)



# # Given an array of Integers identify the maximum occurring element. 
# # Example:
# # Input : [5,5,4,1,1,1,6,7,8], Output : 1
# # Input : [5] , Output: 5
# # Input: [1,2,2,3,3] , Output : [2,3]
# # Input : [], Output: ‘invalid input’






# def max_occuer_element(arr):
#     if len(arr) == 0:
#         print("invalid")
#         return
#     dic = {}
#     for i in range(0, len(arr)):
#         if arr[i] in dic:
#             dic[arr[i]] = dic[arr[i]] + 1
#         else:
#             dic[arr[i]] = 1
    
#     result = []
#     max_count = 0   
    
#     for key in dic:
#         if dic[key] > max_count:
#             max_count = dic[key]
#             result = [key]     
#         elif dic[key] == max_count:
#             result.append(key)
    
#     if len(result) == 1:
#         print(result[0])
#     else:
#         print(result)
# max_occuer_element([1,2,2,3,3])







# # 24)


# # Input Description: 5 X 3 matrix
# # Output Description:
# # The row index(es) with maximum wickets. Row index starts at 1.
# # count wickket and print row 




# def bowling_stats(pitch):
#     if len(pitch) == 0:
#         print("invalid")
#     else:
#         res = 0
#         max_count = 0
#         for i in range(len(pitch)):
#             curr_count = 0
#             for j in range(len(pitch[i])):
#                 if pitch[i][j] == "W":
#                     curr_count = curr_count  + 1
#             if curr_count > max_count:
#                 max_count = curr_count
#                 res = i+1
#         print(res)
    




# bowling_stats(
# [
#     ["B", "B", "B"],
#     ["B", "W", "B"],
#     ["W", "B", "B"],
#     ["B", "W", "B"],
#     ["W", "W", "B"]])







# # 25)

# # n = 4
# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4



# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()
# pattern(4)