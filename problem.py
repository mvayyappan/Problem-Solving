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



