# 1))


# Example 1:
# Input: nums = [1,2,3,1]
# Output: 3
# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 2, 6
        


# ar = [10, 98, 3, 33, 12, 22, 21, 11]
# arr = []
# arrr = []
# for i in range(len(ar)):

#     if ar[i]%2==0:
#         arr.append(ar[i])
#     else:
#         arrr.append(ar[i])
# for i in range(len(arrr)):
#     arr.append(arrr[i])

# print(arr)





# 2))


# socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# counts = {}  # count of each color
# for sock in socks:
#     if sock in counts:
#         counts[sock] = counts[sock] + 1
#     else:
#         counts[sock] = counts[sock] + 1    
# print(counts)




# 3))



# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums3 = [7, 8, 9]
# arr = []
# for i in range(len(nums1)):
#     sum =  nums1[i] + nums2[i] + nums3[i]
#     arr.append(sum)
# print(arr)







# 4))



# l = ["hello", "world"]
# arr = []
# ar = []
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         ar.append(l[i][j])
#     arr.append(ar)
#     ar = []
# print(arr)










# 5))



# ar = ["a","B","c","D","e","F"]
# du = []
# result = []
# for i in range(len(ar)):
#     if ar[i] not in du:
#         du.append(ar[i])
#     print(du)
# for i in range(len(du)):
#     ascii = ord(du[i])
#     if 97 <= ascii <=122:
#         result.append(chr(ascii-32))
#     elif  65 <= ascii <= 90:
#         result.append(chr(ascii+32))


# print(result)  





# 6))



# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2 = [2, 2, 3, 4, 2, 6, 7, 9]
# count = 0
# for i in range(len(l1)):
#     if l1[i] == l2[i]:
#         count = count + 1
# print(count)







# 7))

# l = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
# arr = []
# ar = []
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         a = l[i][j]**2
#         ar.append(a)
#     arr.append(ar)
#     ar = []
# print(arr) 







# 8))

# # Input: aaabbbbcccaaa
# # output: a3b4c3a3



# def compress_string(s):
#     arr = []
#     count1 = -1
#     arr.append((s[0]))
#     for j in range(len(s)):
#         if arr[-1] == s[j]:
#             count1 = count1 + 1
#         elif arr[-1] != s[j]:
#                 arr.append(str(count1+1))
#                 count1 = 0
#                 arr.append(s[j])
#     arr.append(str(count1+1))
#     if len(arr)>=len(s):
#          print(s)
#     else:
#         for i in range(len(arr)):
#             print("".join(arr[i]),end="")
                
# compress_string(('aaabbbbcccaaa'))
    










# # 9))


# # Input: str1 = "Listen", str2 = "Silent"
# # output: True


# def is_anagram(str_1,str_2):
#     str1 = str_1.replace(" ","").lower()
#     str2 = str_2.replace(" ","").lower()

#     if len(str1) != len(str2):
#         print(False)
#     else:
#         count1 = {}
#         count2 = {}
#         for i in range(len(str1)):
#             if i in count1:
#                 count1[str1[i]] = count1[str1[i]] + 1
#             else:
#                 count1[str1[i]] = 1
#         for j in range(len(str2)):
#             if j in count2:
#                 count2[str2[j]] = count2[str2[j]] + 1
#             else:
#                 count2[str2[j]] = 1
#         print(count1)
#         print(count2)
#         if count1 == count2:
#             print(True)
#         else:
#             print(False)


# is_anagram("Listen", "Silent")
# is_anagram("Listens", "silence")
# is_anagram("Hello", "World")






# # 10))


# str1 = "Hollo"
# count = {}
# for i in range(len(str1)):
#     if str1[i] in count:
#         count[str1[i]] = count[str1[i]] + 1
#     else:
#         count[str1[i]] = 1


# result = True

# for i in count.values():
#     if i >=2:
#         result = False
#         break
# print(result)




# # 11))


# # *       * 
# # * *     *
# # *   *   *
# # *     * *
# # *       *


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or i == j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# A = [[1,2,3],[4,5,6],[0,4,5]]
# row = len(A)
# col = len(A)
# B = [[0]*col]*row
# result = [0*col]*row
# for i in range(0,len(A),+1):
#     for j in range(0,len(A[i]),+1):
#         if A[i][j] != 0:
#             result = A
#         else:
#             result = B
#             break
# print(result)


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





# def unique_index(s):
#     count = {}
#     if len(s) == 0:
#         print("invalid input")
#     elif len(s) == 1:
#         print(0)
#     else:
#         for i in range(0,len(s),+1):
#             if s[i] in count:
#                 count[s[i]] = count[s[i]] + 1
#             else:
#                 count[s[i]] = 1
#     print(count)
#     for i in range(0, len(s)):
#         if count[s[i]] == 1:
#             print(i)

#     return -1


# unique_index("aa1b1bcc")




# 1))

# # Input: a = [[1,2], [3,4,5],[6]]
# # Output: 1, 2, 3, 4, 5, 6,


# a = [[1,2], [3,4,5],[6]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end=" ")









# 2))

# # Input: a = [1, 2, 3], b = [4, 5, 6,]
# # Output: 32
# # Logic: (1*4 + 2*5 + 3*6)


# a = [1, 2, 3]
# b = [4, 5, 6,]
# sum = 0
# for i in range(len(a)):
#     sum = sum + a[i]*b[i]
# print(sum)







# # 3))

# # Input: a = [1, 2, 3]
# # Output: 
# # \n 1, 1
# # \n 1, 2 
# # \n 1, 3 
# # \n 2, 1 
# # \n 2, 2 
# # \n 2, 3 
# # \n 3, 1 
# # \n 3, 2 
# # \n 3, 3


# a = [1, 2, 3]
# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[i] ,",", a[j],end="")
#         print(" /n",end=" ")
    






# # 4)) 

# # Input: a = [1, 2, 3, 4]
# # Output: [1, 3, 6, 10]


# a = [1, 2, 3, 4]
# sum = 0
# print("[")
# for i in range(len(a)):
#     sum = sum + a[i]
#     print(sum,",",end=" ")
# print("]")







# # 5))

# # Input: n = 27
# # Output: Factors = 1, 3, 9, 



# n = int(input("enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)








# # 6))

# # Input:  d = {“Samarth”:[45, 60, 50, 90, 70], “Jatin”: [90, 95, 93, 91, 90], “Nishant”:[93, 99, 98, 97, 91]}
# # Output: Jatin Average is 91.8
# #         Nishant Average is 95.6




# d = {"Samarth":[45, 60, 50, 90, 70], "Jatin": [90, 95, 93, 91, 90], "Nishant":[93, 99, 98, 97, 91]}
# sum = 0
# avg =0
# for i,j in d.items():
#     for k in j:
#         sum = sum + k 
#     avg =sum/len(j)
#     sum = 0
#     if avg > 90:
#         print(i , avg)









# # 7))

# # Input: a = [1, 2, 2, 3, 4, 4, 5]
# # Output: 5


# a = [1, 2,2, 2, 3, 4, 4, 5]
# count = 0
# arr = []

# for i in a:
#     if i not in arr:
#         arr.append(i)
#         count = count + 1
# print(count)








# # 8))

# # Input: string = ‘hello, n = 3
# # Output: “Khoor”
# # Logic: Each alphabet is shifted by 3 positions.

# n=3
# txt = "hello"
# str = "abcdefghijklmnopqrstuvwxyz"
# for i in range(len(txt)):
#     for j in range(len(str)):
#         if txt[i] == str[j]:
#             print(str[j+n])










# # 9))

# # Input: len_list = 5
# #                 list = ["a", "b", "y", "e", "p"]
# #                 search_element = "g"
# #                     Output: "Element not found"
# #                 search_element = "e"
# #                     Output: ["a", "b", "y", "p"]
       
        

# list = ["a", "b", "y", "e", "p"]
# search_element = "g"
# if search_element in list:
#     for i in range(len(list)):
#         if list[i] !=search_element:
#             print(list[i])
# else:
#     print("not found")






  

# # 10))


# # Input: n = 5, d = 2
# #     Logic: 2 + 22 + 222 + 2222 + 22222 
# #     Output: 24690


# n = 5
# d = 2
# sum = 0
# sum1 = 0
# for i in range(n):
#     sum = sum + d
#     d = d * 10
#     sum1 = sum1 + sum 
# print(sum1)







# # 11)

# # Input: "Python is great"
# # Output : P - 1 , y - 1 , t -2 ,..

# text = "Python is great"

# visited = ""

# for i in range(len(text)):
#     ch = text[i]

#     if ch == " ":
#         continue

#     if ch in visited:
#         continue

#     count = 0
#     for j in range(len(text)):
#         if text[j] == ch:
#             count += 1

#     print(f"{ch} - {count}")
#     visited += ch








# # 12))

# # names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
# # ages = [24, 21, 23, 20]
# # output:{'MANISH': 24, 'SAMARTH': 21, 'AYUSH': 23, 'ANANYA': 20}



# names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
# ages = [24, 21, 23, 20]
# name_age = {}


# for i in range(len(names)):
#     name_age[names[i]] = ages[i]

# print(name_age)







# # 13))

# # names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
# # Output:{'MANISH': 'AI', 'SAMARTH': 'AA', 'AYUSH': 'AU', 'ANANYA': 'AAA'}



# names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
# result = {}


# for i in range(len(names)):
#     vowels = ""
#     for j in range(len(names[i])):
#         if names[i][j] in "AEIOU":
#             vowels += names[i][j]
#     result[names[i]] = vowels
# print(result)






# # 14))


# # data = [['MANISH', 2], ['SAMARTH', 3], ['AYUSH', 4]]
# # Output : ol = ['MA', 'SAM', 'AYUS']


# data = [['MANISH', 5], ['SAMARTH', 3], ['AYUSH', 4]]
# ol = []
# for i in range(len(data)):
#     word = data[i][0]
#     count = data[i][1]
#     ol.append(word[:count])
# print(ol)







# # 15))
   

# # names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
# # Output: [['MANISH', 6], ['SAMARTH', 7], ['AYUSH', 5], ['ANANYA', 6]]
                


# names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
# count = 0
# output = []


# for i in range(len(names)):   
#     count = 0
#     for ch in names[i]:       
#         count += 1
#     output.append([names[i], count])
# print(output)







# # 16))

# # lnames = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Cache']
# # Output:['Manish', 'Ananya', 'Jyotika', 'Cache']


# names = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Cache']
# result = []

# for  i in range(len(names)):
#     result.append(names[i][3:])
# print(result)








# # 17))


# # lnames = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Coehen']
# # Output:{'Manish': 'Male', 'Ananya': 'Female', 'Jyotika': 'Female', 'Coehen': 'Male'}

# names = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Coehen']
# result = {} 

# for i in range(len(names)):
#     if names[i][0] == "M" and names[i][1] == "r":
#         result[names[i][3:]] = "Male"
#     else:
#         result[names[i][3:]] = "Female"
        
# print(result)






# # 18))

# # d = {
# # 1: ['Nitin', 35, 61, 'Gurgaon'],
# # 2: ['Manish', 34, 55, 'Delhi'],
# # 3: ['Abhishek', 36, 50, 'Noida']
# # }
# # Output: Nitin –> [35, 61]  Manish –> [34, 55]   Abhishek –> [36, 50]



# d = { 1: ['Nitin', 35, 61, 'Gurgaon'], 2: ['Manish', 34, 55, 'Delhi'], 3: ['Abhishek', 36, 50, 'Noida'] }
# list = []

# for i in d.values():
#     list.append(i[1])
#     list.append(i[2])
#     print(i[0], "->",list)
#     list = []







# # 19))

# # lnames = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Coehen']
# # Output: ManMale1 AnaFemale2 JyoFemale3 CoeMale4


# names = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Coehen']
# male = 0

# for i in range(len(names)):
#     if names[i][0] == "M" and names[i][1] == "r":
#         male = male + 1
#         print(names[i][3:6],"Male",male)
#     else:
#         male = male + 1
#         print(names[i][3:6],"Female",male)







# # 20))


# # passList = ['ManMale1', 'AnaFemale2', 'JyoFemale3', 'CoeMale4', 'ManMale5']
# # nameList = ['Manish', 'Ananya', 'Jyotika', 'Coehen', 'Maninder']
# # Expected Output:
# # ol = [['Manish', 'Male', 1],
# # ['Ananya', 'Female', 2],
# # ['Jyotika', 'Female', 3],
# # ['Coehen', 'Male', 4],
# # ['Maninder', 'Male', 5]]



# passlist = ['ManMale1', 'AnaFemale2', 'JyoFemale3', 'CoeMale4', 'ManMale5']
# namelist = ['Manish', 'Ananya', 'Jyotika', 'Coehen', 'Maninder']
# result = []
# arr = []

# for i in range(len(passlist)):
#     arr.append(namelist[i])
#     arr.append(passlist[i][3:-1])
#     arr.append(passlist[i][-1])
#     result.append(arr)
# print(result)






# Reverse Vowels of String :* 
# # Example 1:
# # Input: s = "IceCreAm"
# # Output: "AceCreIm"
# # Example 2:
# # Input: s = "leetcode"
# # Output: "leotcede"
 


# s = "leetcode"

# ar = []
# ar1 = []
# for i in range(0,len(s),+1):
#     if s[i] in "AEIOUaeiou":
#         ar.append(s[i])
#     ar1.append(s[i])
# arr = []
# for j in range(len(ar)-1,-1,-1):
#     arr.append(ar[j])
# print(arr)
# count = 0
# for k in range(0,len(ar1)):
#     if ar1[k] in "AEIOUaeiou":
#         ar1[k] = arr[count]
#         count = count + 1
# print("".join(ar1))







# # Largest 3 same Digit Number in String :* 
# # Example 1:
# # Input: num = "6777133339"
# # Output: "777"
# # Example 2:
# # Input: num = "2300019"
# # Output: "000"
# # Example 3:
# # Input: num = "42352338"
# # Output: ""





# num = "67771839"
# count = 1
# arr = []
# for i in range(1,len(num)):
#     if num[i-1] == num[i]:
#         count = count + 1
#         if count == 3:
#             arr.append(num[i])
#     else:
#         count = 1
# if len(arr) >=1:
#     max = arr[0] 
#     for i in range(0,len(arr)):
#         if arr[i]>max:
#             max=str(arr[i])
#     print(max*3)
# else:
#     print("No")








# Find the Town Judge :*

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
 
# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 
# Constraints:
# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n

# — 




# You are going on an expedition and need to find the best camping site on a 2D map of the area. The map is represented as a grid, where each cell is marked with specific symbols that indicate the terrain or resources available at that location. Your task is to find an empty spot suitable for camping that meets at least 2 of the following conditions:
# ﻿﻿﻿The site is near water (W).
# ﻿﻿﻿The site is near trees (T).
# ﻿﻿﻿The site is near rocks (R).
# Two locations are considered "nearby" if they are adjacent either horizontally or vertically (not diagonally). You must identify if there is an empty spot (E) that meets at least two of these conditions.
# Write a function find_best_camping_site(map_grid) that returns the coordinates of the best camping spot. If there are multiple such spots, return any of them. If no suitable spot is found, return (-1, -1).
# Input:
# ﻿﻿map_grid: A 2D list representing the map of the expedition area, where:
# ﻿﻿'E' represents an empty spot.
# ﻿﻿'W' represents water.
# ﻿﻿'T' represents trees.
# ﻿﻿'R' represents rocks.
# ﻿﻿Other characters may represent obstacles or unusable terrain.

# Output:
# * Return a tuple (x, y) representing the coordinates of an empty spot that meets at least two of the conditions (near water, trees, or rocks). If no such spot exists, return (-1, -1).

# Example
# Input:
# map-grid_1 = l
# ['E, W', 'E', 'T'],
# ['R', 'E, 'T', 'E'], [‘E’, 'E, W', 'E'], [T', 'E, 'E, 'R']
# Output:
# (1, 1) (This spot has water and trees nearby)
# Input2 :
# map-grid_2 = l
# [R', 'E, 'T', 'R],
# [T', 'E, 'E, 'W],
# ['E, 'E, W', 'E], ['R', 'E, T','E]
# Output2 :
# (1, 2) (This spot has water and trees



# # 1)) sum list


# def sum_list(l):
#     sum = 0
#     for i in range(len(l)):
#         sum = sum + l[i]
#     print(sum)

# sum_list([1,2,3,4,5])











# # 2)) sum list +num

# def sum_list_positive_numbers(l):
#     sum = 0
#     for i in range(len(l)):
#         if l[i] >=0:
#             sum = sum + l[i]
#     print(sum)
# sum_list_positive_numbers([-1,-2,-3,-4,-5,1,2,3,4,5])








# # 3)) sum list multiple of 3


# def sum_list_multiple_of_3(l):
#     sum = 0
#     for i in range(len(l)):
#         if l[i]%3==0:
#             sum = sum + l[i]
#     print(sum)
# sum_list_multiple_of_3([1,2,3,4,5,6,7,8,9,0])









# # 4))  sum a nested list

# def sum_nested_list(l):
#     sum = 0
#     for i in range(len(l)):
#         for j in range(len(l[i])):
#             sum = sum + l[i][j]
#     print(sum)
# sum_nested_list([[1,2,3],[4,5,6],[7,8,9],[10]])











# # 5))  sum of digit in each element 


# def sum_of_digit_in_each_element_in_list(l):
#     result = []
#     sum = 0
#     for n in l:
#         sum = 0
#         while n>0:
#             digit = n%10
#             sum = sum + digit
#             n = n//10
#         result.append(sum)
#     print(result)
# sum_of_digit_in_each_element_in_list([123,456,789,0])









# # 6) multiple of all items im list


# def multiple_list(l):
#     mul = 1
#     for i in range(len(l)):
#         mul = mul*l[i]
#     print(mul)
# multiple_list([1,2,3,4,5])











# # 7) multiple of odd numbers

# def multiple_odd(l):
#     mul = 1
#     for i in range(len(l)):
#         if l[i]%2==1:mul = mul * l[i]
#     print(mul)
# multiple_odd([1,2,3,4,5])










# # 8) multiple of items ignore zero

# def multiple_items_ignore_zero(l):
#     multi = 1
#     for i in range(len(l)):
#         if l[i] != 0:
#             multi = multi*l[i]
#     print(multi)
# multiple_items_ignore_zero([1,2,3,4,5,0])










# # 9) multiple_items in list but without using loop


# def product(lst):
#     if len(lst) == 1:        
#         return lst[0]
#     return lst[0] * product(lst[1:])

# numbers = [2, 3, 4, 5]
# print(product(numbers))





# # 10)

# def cumulative_product(l):
#     mul = 1
#     lst = []
#     for i in range(0,len(l),+1):
#         mul = mul * l[i]
#         lst.append(mul)
#     print(lst)
# cumulative_product([1,2,3,4])






# # 11) maximum number


# def max(l):
#     max = l[0]
#     for i in l:
#         if i>max:
#             max = i
#     print(max)
# max([1,2,3,4,5])

    







# # 12) second maximum number

# def second_max(l):
#     if len(l) == 1:
#         print("not a second max")
#     else:
#         max = l[0]
#         for i in l:
#             if i>max:
#                 max = i
#         sec_max=l[0]
#         for j in l:
#             if j>sec_max and max!=j:
#                 sec_max=j
#         print(sec_max)
# second_max([1,2,3,4]) 
        








# # 13)  maximum number multiple of 5



# def max(l):
#     max = l[0]
#     for i in l:
#         if i>max and i%5==0:
#             max = i
#     print(max)
# max([1,2,13,10,5])









# # 14)  unique maximum number

# def unique_max(l):
#     count = {}
#     if len(l) == 0:
#         print("invalid")
#     elif len(l) == 1:
#         print(l[0])
#     else:
#         for i in range(0,len(l),+1):
#             if l[i] in count:
#                 count[l[i]] += 1
#             else:
#                 count[l[i]] = 1
#     found = 0
#     result = -999999999   
#     for key in count:
#         if count[key] == 1:
#             if found == 0:
#                 result = key
#                 found = 1
#             else:
#                 if key>result:
#                     result = key
#     if found == 0:
#         print("no unique number")
#     else:
#         print("unique max number:", result)

        
# unique_max([1,2,3,4,5,5,4,3,2])









# # 15)  maximum even number 



# def max(l):
#     max = l[0]
#     for i in l:
#         if i>max and i%2==0:
#             max = i
#     print(max)
# max([1,2,13,10,5])






# # 16)  minimum  number 



# def min(l):
#     min = l[0]
#     for i in l:
#         if i<min:
#             min = i
#     print(min)
# min([1,2,13,10,5])










# # 17) second minimum number


# def sec_min(l):
#     min = l[0]
#     for i in l:
#         if i<min:
#             min = i
#     sec_min = l[-1]
#     for j in l:
#         if j<=sec_min and min!=j:
#             sec_min=j
#     print(sec_min)


# sec_min([1,2,3,4,5,6])








# # 18) minimum prime number


# def prime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True

# def min_prime(l):
#     minimum = None
#     for n in l:
#         if prime(n):          
#             if minimum is None or n < minimum:
#                 minimum = n

#     if minimum is None:
#         print("No prime numbers")
#     else:
#         print("Minimum prime:", minimum)

# min_prime([1,4,6,8,9,10])







# 19) missing number in list


