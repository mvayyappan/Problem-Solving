# # 0)



# # ******
# # *   **
# # *  * *
# # * *  *
# # **   *
# # ******

# n = 6 

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1 or j == n  or n-i+1 == j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 1)


# ***  
#   *  
#   *
#   *
# *****

# n = 5 
# mid = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == mid or i == n or (j<=mid and i == 1) :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 2)


# # *****
# #     *
# # *****
# # *
# # *****

# n = 5
# mid = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or i == mid or (i<mid and j == n) or (i>mid and j == 1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 3)


# # *****
# #     *
# # *****
# #     *
# # *****


# n = 5
# mid = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == mid or i == n or j == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
     





# # 4)

# # *   *
# # *   *
# # *****
# #     *
# #     *

# n = 5
# mid = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == n or i == mid or (i<=mid and j == 1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
        






# # 5)


# # *****
# # *    
# # *****
# #     *
# # *****


# n = 5 
# mid =  n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == mid or i == n or (i<mid and j == 1) or (i>mid and j == n):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 6)


# # *****
# # *    
# # *****
# # *   *
# # *****

# n = 5
# mid =  n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == mid or i == n or (i<mid and j == 1) or (i>mid and (j == n or j == 1) ):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()







# # 7)

# # *****
# #    * 
# #   *
# #  *
# # *


# n = 5
# mid =  n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or n-i+1 == j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# # 8)


# # *****
# # *   * 
# # *****
# # *   *
# # *****




# n = 5
# mid =  n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == mid or i == n or (i<mid and (j == 1 or j==n)) or (i>mid and (j == n or j == 1) ):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# # 9)


# # *****
# # *   *
# # *****
# #     *
# # *****

# n = 5
# mid =  n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == mid or i == n or (i<mid and (j == 1 or j == n)) or (i>mid and j == n ):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


