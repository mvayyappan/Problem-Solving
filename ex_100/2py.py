# # 1)

# # move zeros end with out list:


# def move_zeros(l):
#     index = 0
#     count = 0
#     for i in range(0,len(l)):
#         if l[i] == 0:
#             count = count + 1
#         else:
#             l[index] = l[i]
#             index = index + 1
#     for i in range(index,len(l),+1):
#         l[i] = 0
#     print(l)
    
# move_zeros([0,0,0,3,12])








# # 2)


# # input: aabcccccaaa 
# #output : a2b1c5a3


# s = "aabccccaaa"

# result = []
# result.append(s[0])
# count = 0
# for i in range(len(s)):
#     if s[i] == result[-1]:
#         count = count + 1
#     else:
#         result.append(str(count))
#         result.append(s[i])
#         count = 1
# result.append(str(count))

# print("".join(result))













