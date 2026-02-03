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




