# # # 1)

# # find a mirror letter in a to z:

# # example :  "abc" -> "zyx"  , dza -> waz

# txt = "abcdaz"
# for i in range(len(txt)):
#     res = chr((ord('a')+ord('z'))-ord(txt[i]))
#     print(res,end=" ")









# # 2) add end to 9 to 0 

# # ex: 1234 -> 1+2+3+4 -> 1+0 -> 1 , 99999 -> 9+9+9+9+9 -> 4+5 -> 9



# def zero(n):
#     sum = 0
#     while n>0:
#         digit = n%10
#         sum = sum + digit
#         n = n // 10 
#     return sum


# def nine(n):
#     if n<10:
#         print(n)
#     else:
#         res = zero(n)
#         nine(res)

# nine(123456789)








# # # 3) alternative primme numbers


# # Example -> 1 to 10 find prime and add alternatevie
# # 2-3+5-7 = -3


# n = 10
# notprime = []
# prime= []
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j == 0:
#             notprime.append(i)
#             break
#     else:
#         prime.append(i)

# add = 0
# z = 1
# for i in range(len(prime)):
#     add = add  +  (z*prime[i])
#     z = -z
# print(add)








# # # 4) find sub palindrome


# s = "abcbd"
# found = False

# for i in range(len(s)):
#     for j in range(i+3, len(s)+1):
#         sub = s[i:j]
#         if sub == sub[::-1]:
#             found = True
#         print(sub)







# 5. Frequency Sort Without Built-in

# Problem:
# Sort characters in a string based on frequency.

# Example:
# Input: "tree"
# Output: "eert" or "eetr"

# (e appears twice)



s = "tree"
count = 0







# 6. Rotate Digits Maximum Number

# Problem:
# Rotate digits of a number and find the maximum possible rotation value.

# Example:
# Input: 1976

# Rotations:
# 1976
# 9761
# 7619
# 6197

# Output: 9761












# 7. First Non-Repeating Word

# Problem:
# Given a sentence, find the first word that does not repeat.

# Example:
# Input:
# "this is a test this is only test"

# Output:
# "a"

# 8. Zigzag Array Transformation

# Problem:
# Convert array into zigzag format.

# Condition:
# a < b > c < d > e

# Example:
# Input: [4,3,7,8,6,2,1]
# Output: [3,7,4,8,2,6,1]

# 9. Missing Character in Alphabet

# Problem:
# Given a string containing letters a-z, find which letters are missing.

# Example:
# Input: "abcdefxz"

# Output:
# g h i j k l m n o p q r s t u v w y

# 10. Reverse Words but Keep Positions

# Problem:
# Reverse letters but keep spaces in same index.

# Example:

# Input:
# "ab cd ef"

# Output:
# "fe dc ba"


