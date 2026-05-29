# # PRINT A PATTERN

# n = int(input("enter a number:"))
# for i in range(1,n+1,+1):
#     for j in range(1,i+1,+1):
#         print("*",end="")
#     print()





# #  SATURATED OR NOT [-> MAKE EXACTLY TWO DIGITS]

# n = int(input("enter a  number:"))
# list = []
# while n>0:
#     digit = n%10
#     if digit not in list:
#         list.append(digit)
#     n = n//10
# if len(list) == 2:
#     print("Saturated")
# else:
#     print("UnSaturated")
    




# # second maximum  number in a list


# lst = input("enter list of number:")
# lst = lst.split(",")
# print(lst)

# max = lst[0]
# sec_max = lst[0]

# for i in range(0,len(lst)):
#     if max < lst[i]:
#         max= lst[i]
# for j in range(0,len(lst)):
#     if sec_max<lst[j] and max!=lst[j]:
#         sec_max = lst[j]
# print(sec_max)






# # Divisible By Previous Integer previous integer

# lst = [1,2,3,6,7]
# result = []
# for i in range(1,len(lst),+1):
#     if lst[i]%lst[i-1] == 0 :
#         result.append(lst[i])
# print(result)






# # remove repeating characters

# s = "mississipie"
# count = {}
# for i in range(0,len(s)):
#     if s[i] not in count:
#         count[s[i]] = 1
#     else:
#         count[s[i]] = count[s[i]] + 1
# res = []
# for j in count:
#     if count[j] == 1:
#         res.append(j)
# res= "".join(res)
# print(res)









s1 = "abcde"
s2 = "bcdea"
res = False
if len(s1) == len(s2): 
    for i in range(0,len(s1)):
        temp = ""
        temp =  s1[i:] + s1[:i]
        if s2 == temp:
            res = True
            break
print(res)