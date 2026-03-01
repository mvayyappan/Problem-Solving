# # # 1))


# # Enter the row size for the pattern: 5
# #    * 
# #    * * 
# #    * * * 
# #    * * * * 
# #    * * * * * 




# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()








# # # 2))

# # Enter the row size for the pattern: 5
# #    * * * * * 
# #    * * * *
# #    * * *
# #    * *
# #    *




# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()








# # # 3))


# # Enter the row size for the pattern: 5
# #            * 
# #          * * * 
# #        * * * * * 
# #      * * * * * * * 
# #    * * * * * * * * * 


# n=int( input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(i*2-1):
#         print("*",end="")
#     print()







# # # 4))


# # # Enter the row size for the pattern: 5
# #    * * * * * * * * * 
# #      * * * * * * *
# #        * * * * *
# #          * * *
# #            *


# n=int( input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(i*2-1):
#         print("*",end=" ")
#     print()







# # # 5)

# Enter the row size for the pattern: 4
# #          * 
# #        * * * 
# #      * * * * * 
# #    * * * * * * * 
# #      * * * * * 
# #        * * * 
# #          * 



# n=int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(i*2-1):
#         print("*",end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(i*2-1):
#         print("*",end=" ")
#     print()






# # # 7)


# # Enter the row size for the pattern: 5
# #    * * * * * 
# #    *       * 
# #    *       * 
# #    *       * 
# #    * * * * * 



# n = int(input("enter  a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or j == 1 or i == n or j == n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()




# # # 8)


# # Enter the row size for the pattern: 5
# #    * 
# #    * * 
# #    *   * 
# #    *     * 
# #    * * * * * 


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j == 1 or i == n or i == j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()








# # # 9)

# Enter the row size for the pattern: 5
#    * * * * * 
#    *       * 
#    *       * 
#    *       * 
#    * * * * * 


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1 or j == n: 
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()








# # # 10)


# # Enter the row size for the pattern: 5
# #    * * * * 
# #    *   * 
# #    * * 
# #    * 


# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if j == 1 or i == n or i == j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()








# # # 11)


# # Enter the row size for the pattern: 5

# #            * 
# #          *   * 
# #        *       * 
# #      *           * 
# #    * * * * * * * * * 



# n = int(input("enter a number:"))

# for i in range(1,n+1):  
#     for j in range(n-i):  
#         print(" ", end=" ")
#     for k in range(1,2*i):
#         if k == 1 or k == 2 * i - 1 or i == n:  
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()









# # # 12)



# #    * * * * * * * * * 
# #      *           *
# #        *       *
# #          *   *
# #            *




# rows = int(input("enter a number:"))

# for i in range(rows,0,-1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()







# # # 13))


# #            * 
# #          *   *
# #        *       *
# #      *           *
# #    *               *
# #      *           *
# #        *       *
# #          *   *
# #            *






# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows+1): 
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         if k == 1 or k == 2 * i - 1 : 
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()

# for i in range(rows-1,0,-1):  
#     for j in range(rows  - i): 
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         if k == 1 or k == 2 * i - 1 : 
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()









# # #14)))


# # Enter the row size for the pattern: 5
# # *                 * 
# # * *             * * 
# # * * *         * * * 
# # * * * *     * * * * 
# # * * * * * * * * * * 
# # * * * * * * * * * * 
# # * * * *     * * * * 
# # * * *         * * * 
# # * *             * * 
# # *                 * 

# n = int(input("enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(1,n+1-i):
#         print(" ",end=" ")
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(1,n+1-i):
#         print(" ",end=" ")
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()








# # # 15)))




# # Enter the row size for the pattern: 5
# # *                 * 
# # * *             * * 
# # *   *         *   * 
# # *     *     *     * 
# # *       * *       * 
# # *       * *       * 
# # *     *     *     * 
# # *   *         *   * 
# # * *             * * 
# # *                 * 




# n = int(input("enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(1,n+1-i):
#         print(" ",end=" ")
#     for l in range(1,n+1-i):
#         print(" ",end=" ")
#     for m in range(1,i+1):
#         print("*",end=" ")

#     print()

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(1,n+1-i):
#         print(" ",end=" ")
#     for l in range(1,n+1-i):
#         print(" ",end=" ")
#     for m in range(1,i+1):
#         print("*",end=" ")
#     print()






# # # 16))


# # enter a number:9
# # *       *
# #  *     *
# #   *   *
# #    * *
# #     *
# #    * *
# #   *   *
# #  *     *
# # *       *






# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j or n-i+1 == j :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()








# # # 17)))

# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *


# n = int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# n = int(input("enter a number: "))

# for i in range(1, n + 1):

#     for j in range(1, n + 1 - i):
#         print(" ", end=" ")

#     for k in range(1, i + 1):
#         print("*", end=" ")

#     print()










# # # 18))

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# n = int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(1,n+1-i):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(1,n+1-i):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()


















# # # 19)


#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *




# n = int(input("enter  a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(1,i*2+1):
#         if 1 == k or k == 2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for k in range(1,i*2+1):
#         if 1 == k or k == 2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()













# # # 20)))




# #    *********
# #     *     *
# #      *   *
# #       * *
# #        *
# #       * *
# #      *   *
# #     *     *
# #    *********



# n = int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j or j == n+1-i or i == 1 or i == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# 1)



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or  i == n or j == n or j == 1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    

# 2)


# n= int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


#      *
#     * *
#    *   *
#   *     *
#  *       *
# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *





