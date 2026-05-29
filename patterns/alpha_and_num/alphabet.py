# # 1)

# #     *
# #    * *
# #   *****
# #  *     *
# # *       *

# n = 5

# for i in range(1,n+1):
#     for k in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if j == 1 or j == 2*i-1 or i == (n//2)+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 2)


# # **** 
# # *   *
# # *****
# # *   *
# # ****



# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == 1 or (i == 1 or i == n or i == n // 2 + 1) and j <= n - 1:
#             print("*", end="")
#         elif i != 1 and i != n and j == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# # 3)

# # *****
# # *    
# # *
# # *
# # *****


# n = 5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 4)

# # *****
# # *   *
# # *   *
# # *   *
# # *****


# n= 5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 5)



# # *****
# # *    
# # *****
# # *
# # *****


# n = 5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or j == 1 or i == n//2+1 or i == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# # 6)



# # *****
# # *    
# # *****
# # *
# # *


# n = 5


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or j == 1 or i == n//2+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# # 7)


# # *****
# # *    
# # * ***
# # *   *
# # *****


# n = 5

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == 1 or i == 1 or i == n or (i > n // 2 and j == n) or (i == (n // 2 + 1) and j > n // 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()





# # 8)

# # *   *
# # *   *
# # *****
# # *   *
# # *   *



# n = 5

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == n//2+1 or j == 1 or j == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
 



# # 9)


# # *****
# #   *  
# #   *
# #   *
# # *****

# n = 5

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == n//2+1 or i == 1 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()




# # 10)



# # *****
# #   *  
# #   *
# #   *
# # ***

# n = 5

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == n//2+1 or i == 1 or (i == n and j<n//2+1) :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()







# # 11)

# # * *
# # ** 
# # *  
# # ** 
# # * *

# n = 5
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n//2+2):
#         if j == 1 or j == x:
#             print("*",end="")
#         else:
#             print(" ",end="") 
#     if i<=n//2:
#         x=x-1
#     else:
#         x=x+1
#     print()







# # 12)


# # *    
# # *    
# # *    
# # *    
# # *****

# n = 5

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == n or j == 1 :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()







# # 13)


# # *     *
# # **   **
# # * * * *
# # *  *  *
# # *     *
# # *     *
# # *     *

# n = 7
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or (i == j and i<n//2+2) or (j == n-i+1 and i<n//2+2) :
#             print("*",end="")
#         else:
#             print(" ",end="") 








# # 14)


# # *     *
# # **    *
# # * *   *
# # *  *  *
# # *   * *
# # *    **
# # *     *


# n = 7
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or j == i :
#             print("*",end="")
#         else:
#             print(" ",end="") 







# # 15)


# # *****
# # *   *
# # *   *
# # *   *
# # *****

# n = 5
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or i == 1 or i == n :
#             print("*",end="")
#         else:
#             print(" ",end="") 
#     print()







# # 16)


# # *****
# # *   *
# # *****
# # *    
# # *  


# n = 5
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or (j == n and i<=n//2+1) or i == 1 or i == n//2+1 :
#             print("*",end="")
#         else:
#             print(" ",end="") 
#     print()





# 17)

# 18)



# # 19)


# # *****
# # *    
# # *****
# #     *
# # *****

# n = 5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or i == n//2+1 or (j == 1 and i<=n//2) or (j == n and i>n//2+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 20)


# # *****
# #   *  
# #   *  
# #   *  
# #   * 


# n = 5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or j == n//2+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 21)


# # *   *
# # *   *
# # *   *
# # *   *
# # *****


# n = 5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == n or j == 1 or j == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 22)


# # *     *
# #  *   * 
# #   * *  
# #    *  

# n = 7

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i == j and i<=n//2+1) or (n-i+1 == j and i<=n//2+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 23)


# # *     *
# # *     *
# # *     *
# # *  *  *
# # * * * *
# # **   **
# # *     *

# n = 7
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or (i == j and i>n//2) or (j == n-i+1 and i>n//2) :
#             print("*",end="")
#         else:
#             print(" ",end="")
#       print()






# # 24)


# # *     *
# #  *   * 
# #   * *  
# #    *   
# #   * *  
# #  *   * 
# # *     *



# n = 7
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == i or n-i+1 == j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 25)

# # *   *
# #  * * 
# #   *  
# #   *  
# #   *  


# n = 5
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j==i and i<=n//2+1) or (n-i+1==j  and i<=n//2+1)or (j == n//2+1 and i>n//2+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()








# # 26)


# # *****
# #    * 
# #   *  
# #  *   
# # *****


# n = 5
# x = n//2+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if n-i+1 == j or i == 1 or i == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()