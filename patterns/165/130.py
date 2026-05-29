# # 91)


# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *


# n = int(input("enter a number:"))

# for i in range(0,n,+1):
#     for j in range(1,n-i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(1,n-i+1):
#         print("*",end=" ")
#     print()








# # 92)


# # * * * * 
# #  * * * 
# #   * *
# #    *
# #   * *
# #  * * *
# # * * * *


# n = int(input("enter a number:"))



# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end="")
#     for k in range(i,n+1):
#         print("*",end=" ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for k in range(i+1,n+1):
#         print("*",end=" ")
#     print()









# # 93)


# # *       *
# # **     **
# # ***   ***
# # **** ****
# # *********

# n = int(input("enter a number:"))

# for i in range(1,n):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,2*(n-i)):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()
# for m in range(1,n*2):
#     print("*",end="")






# # 94)


# # *********
# # **** ****
# # ***   ***
# # **     **
# # *       *



# n = int(input("enter a number:"))

# for m in range(1,n*2):
#     print("*",end="")
# print()
# for i in range(n-1,-1,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,2*(n-i)):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()







# # 95)

# #     *       *
# #    ***     ***
# #   *****   *****
# #  ******* *******
# # *****************


# n = int(input("enter a number:"))

# for i in range(1,n):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     for l in range(1,n-i):
#         print(" ",end="")
#     for d in range(1,n-i+1):
#         print(" ",end="")
#     for m in range(1,2*i):
#         print("*",end="")
#     print()
# for a in range(1,4*n-2):
#     print("*",end="")




# # 96)


# # 1 2 3 4 * 4 3 2 1 
# # 1 2 3 * * * 3 2 1 
# # 1 2 * * * * * 2 1
# # 1 * * * * * * * 1
# # * * * * * * * * *


# n = int(input("Enter anumber:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(j,end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     for l in range(n-i,0,-1):
#         print(l,end=" ")
#     print()




# # 97)

# #         *
# #       # * #
# #     * # * # *
# #   # * # * # * #
# # * # * # * # * # *


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         if (i+k)%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()







# # 98)


# #        * 
# #       * *
# #      * * *
# #     * * * *
# #    *       *
# #   * *     * *
# #  * * *   * * *
# # * * * * * * * *


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+n+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for l in range(1,2*(n-i)+1):
#         print(" ",end="")
#     for m in range(1,i+1):
#         print("*",end=" ")   
#     print()






# # 99)



# #     *    
# #    * *   
# #   *   *
# #  *     *
# # *********


# n = int(input("enter a number:"))

# for i in range(1,n):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         if k == 2*i-1 or k == 1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# print((2*n-1)*"*")







# # 100)



# # *
# # **
# # * *
# # *  *
# # * *
# # **
# # *


# n = 7
# x = 1
# for i in range(1, n + 1):
#     for j in range(1, x + 1):
#         if j == 1 or j == x:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#     if i <= n // 2:
#         x += 1
#     else:
#         x -= 1







# # 101)

# #     *
# #    **
# #   * *
# #  *  *
# # *   *
# #  *  *
# #   * *
# #    **
# #     *

# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         if i == j or j == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
    
# for i in range(2,n+1):
#     for j in range(1,n+1):
#         if i == j or j == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 102)


# # *********
# #  *     * 
# #   *   *
# #    * *
# #     *


# n = int(input("enter a number:"))

# for a in range(1,2*n):
#     print("*",end="")
# print()

# for i in range(n-1,0,-1):
#     for k in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if j == 1 or j == 2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# # 103)


# # *     *
# # **   **
# # * * * *
# # *  *  *
# # * * * *
# # **   **
# # *     *



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or i == j or  j == n-i+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 104)


# # *  *  *
# #  * * *
# #   ***
# # *******
# #   ***
# #  * * *
# # *  *  *

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j or j == n-i+1 or j == n//2+1 or i == n//2+1:
#             print("*",end="") 
#         else:
#             print(" ",end="")
#     print()







# # 105)


# # *  ****
# # *  *   
# # *  *
# # *******
# #    *  *
# #    *  *
# # ****  *


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i == n//2+1 or j == n//2+1 or (i == 1 and j >=n//2+1 ) or (i == n and j <=n//2+1 ) or (j == 1 and i <=n//2+1 ) or (j == n and i >=n//2+1)):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()








# # 106)

# # * * * *
# # * * * *
# # *******
# # *     *
# # *     *
# # *     *
# # *******


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 3 or i == n or j == 1 or j == n or (i == 1 and j%2==1) or (i == 2 and j%2==1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()








# # 107)

# # *********
# # *       *
# # * ***** *
# # * *   * *
# # * * * * *
# # * *   * *
# # * ***** *
# # *       *
# # *********



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if  i == 1 or i == n or j ==1 or j == n or ((i == 3 or i == 7) and (3 <= j <= 7)) or (j == 3 or j == 7) and (3 <= i <= 7) or i == 5 and j == 5:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # 108)

# #  * * * 
# # * * * *
# #  * * *
# # * * * *
# #  * * *
# # * * * *
# #  * * *


# n = 7
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i + j) % 2 == 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()










# # 109)


# # *     *     *
# # **   ***   **
# # *** ***** ***
# # *************
# # or
# # *************
# # *** ***** ***
# # **   ***   **
# # *     *     *

# n = int(input("enter a number:"))


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,2*(n-i)+2):
#         print(" ",end="")
#     for l in range(1,2*i):
#         print("*",end="")
#     for m in range(1,2*(n-i)+2):
#         print(" ",end ="")
#     for o in  range(1,i+1):
#         print("*",end="")
#     print()

# for p in range(1,4*n+2):
#     print("*",end="")
# print()

# # or 

# for p in range(1,4*n+2):
#     print("*",end="")
# print()
# for i in range(n,-1,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,2*(n-i)+2):
#         print(" ",end="")
#     for l in range(1,2*i):
#         print("*",end="")
#     for m in range(1,2*(n-i)+2):
#         print(" ",end ="")
#     for o in  range(1,i+1):
#         print("*",end="")
#     print()







# # 110)


# #      *
# #     ***
# #    * * *
# #   *  *  *
# #  *   *   *
# # ***********
# #  *   *   *
# #   *  *  *
# #    * * *
# #     ***
# #      *



# n = int(input("entert a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         if k == 1 or k == 2*i-1 or i == k or i == n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for l in range(n-1,-1,-1):
#     for m in range(1,n-l+1):
#         print(" ",end="")
#     for o in range(1,2*l):
#         if o == 1 or o == 2*l-1 or l == o:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()








# # 111)



# # # **********
# # # ****  ****
# # # ***    ***
# # # **      **
# # # *        *
# # # **      **
# # # ***    ***
# # # ****  ****
# # # **********



# n = int(input("entera number:"))

# for i in range(n+1):
#     for j in range(n-i+1):
#         print("*",end="")
#     for k in range(i):
#         print(" ",end="")
#     for l in range(i):
#         print(" ",end="")
#     for m in range(n-i+1):
#         print("*",end="")
#     print()
# for i in range(n-1,-1,-1):
#     for j in range(n-i+1):
#         print("*",end="")
#     for k in range(i):
#         print(" ",end="")
#     for l in range(i):
#         print(" ",end="")
#     for m in range(n-i+1):
#         print("*",end="")
#     print()
    
    
    



# # 112)


# # ********
# # *** ****
# # **   ***
# # *     **
# # **     *
# # ***   **
# # **** ***
# # ********


# n = int(input("entera number:"))

# for i in range(n+1):
#     for j in range(n-i+2):
#         print("*",end="")
#     for k in range(i):
#         print(" ",end="")
#     for l in range(i):
#         print(" ",end="")
#     for m in range(n-i+1):
#         print("*",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i+1):
#         print("*",end="")
#     for k in range(i):
#         print(" ",end="")
#     for l in range(i):
#         print(" ",end="")
#     for m in range(n-i+1):
#         print("*",end="")
#     print()







# # 113)


# # *     *
# # **   **
# # *** ***
# # *******
# # *** ***
# # **   **
# # *     *


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,(2*n)-(2*i)+1):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(1,(2*n)-(2*i)+1):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()



# # 114)


# #     *****
# #    *****
# #   *****
# #  *****
# # *****

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,n+1):
#         print("*",end="")
#     print()






# # 115)


# # **
# # **
# # ****
# # ****
# # ******
# # ******



# n = int(input("entera  number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i<=2 and j<=2:
#             print("*")  





# 116)


#      **
#      **
#    ****
#    ****
#  ******
#  ******




# 117)



# ******
# ******
# ****
# ****
# **
# **




# 118)


# ******
# ******
#   ****
#   ****
#     **
#     **




# 119)


# **
# ****
# ******



# # 120)


# # *
# # *
# # **
# # **
# # ***
# # ***

# for i in range(1, 4):
#     for x in range(2, 0, -1):
#         for y in range(2, i - 1, -1):
#             print(" ", end="")
#         for j in range(i):
#             print("*", end="")
#         print()







# # 121)



# ***
# ***
# **
# **
# *
# *


# for i in range(3, 0, -1):
#     for x in range(2, 0, -1):
#         for j in range(i):
#             print("*", end="")
#         print()









# # 122)

# # ***
# # ***
# #  **
# #  **
# #   *
# #   *

# for i in range(3, 0, -1):
#     for x in range(2, 0, -1):
#         for y in range(2, i - 1, -1):
#             print(" ", end="")
#         for j in range(i):
#             print("*", end="")
#         print()







# # 123)




# #    *
# #    *
# #   ***
# #   ***
# #  *****
# #  *****


# n = 3
# z = 1
# for i in range(n):
#     for j in range(2, 0, -1):
#         for x in range(n - 1, i - 1, -1):
#             print(" ", end="")
#         for y in range(z):
#             print("*", end="")
#         print()
#     z += 2







# # 124)



#       **      
#       **      
#     *    *
#     *    *
#   *        *
#   *        *
# *            *


# n = 7
# x = n
# for i in range(1, n + 1):
#     for j in range(1, 2 * n + 1):
#         if j == x or j == 2 * n - x + 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#     if i % 2 == 0:
#         x -= 2







# # 125)


# *****
#  ***
#   *
#  ***
# *****


# n = 3
# s1 = n * 2 - 1
# s2 = 3
# for i in range(1, n + 1):
#     print(" " * (i - 1), end="")
#     print("*" * s1)
#     s1 -= 2
# for i in range(1, n):
#     print(" " * (n - i - 1), end="")
#     print("*" * s2)
#     s2 += 2








# # 126)


# #     * * * * * *
# #   * * * * * * * *
# #  * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# #  * * * * * * * * *
# #   * * * * * * * *
# #     * * * * * *



# for i in range(1, 10):
#     if i == 1 or i == 9:
#         x = 6
#         z = 4
#     elif i == 2 or i == 8:
#         x = 8
#         z = 2
#     elif i == 3 or i == 7:
#         x = 9
#         z = 1
#     else:
#         x = 10
#         z = 0
#     print(" " * z, end="")
#     print("* " * x)







# # 127)


# #    *** ***
# #  ***** *****
# #  ***********
# #   *********
# #    *******
# #     *****
# #      ***
# #       *



# n = 6
# for i in range(n // 2, n + 1, 2):
#     print(" " * (n - i), end="")
#     print("*" * i, end="")
#     print(" " * (n - i), end="")
#     print("*" * i)
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))






# # 128)


# #  ** ** 
# # *  *  *
# # *     *
# #  *   *
# #   * *
# #    *


# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()








# # # 129)



# #                     * 
# #                    * * 
# #                   * * *
# #                  * * * *
# #                  * * * *
# #                  * * * *
# #                  * * * *
# #                  * * * *
# #                   * * *
# #                  * * * *
# #                 * * * * *
# #                * * * * * *
# #                  * * * *
# #                  * * * *
# #                  * * * *
# #                  * * * *

# height = 3
# width = 4
# space = width * 5
# r = 1
# m = 1
# for r in range(1, height):
#     for i in range(m, width + 1):
#         for j in range(space, i - 1, -1):
#             print(" ", end="")
#         for k in range(1, i + 1):
#             print("* ", end="")
#         print()
#     m += 2
#     width += 2
#     for i in range(1, 5):
#         for j in range(space - 3, 0, -1):
#             print(" ", end="")
#         for k in range(1, 5):
#             print("* ", end="")
#         print()






# # 130)



# # *****
# # *  **
# # * * *
# # **  *
# # *****


# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or i == n or j == 1 or j == n or  j == n-i + 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


