# 61)

# # # # # #
#  * * * *
#   # # #
#    * *
#     #



# n=int(input("enter  a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()





# # 62)


# # # * # * #
# #  * # * #
# #   # * #
# #    * #
# #     #


# n=int(input("enter  a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()






# # 63)


# # 5 5 5 5 5
# #  * * * *
# #   3 3 3
# #    * *
# #     1




# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i %2==0:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#     print()







# # 64)


# # 0
# # 1*
# # 2**
# # 3***
# # 4****
# # 5*****


# n = int(input("enter  a number:"))

# for i in range(0,n+1):
#     for j in range(1,i+2):
#         if j==1:
#             print(i,end="")
#         else:
#             print("*",end="")
#     print()





# # 65)


# # 5*****
# # 4****
# # 3***
# # 2**
# # 1*
# # 0


# n = int(input("enter  a number:"))

# for i in range(n,-1,-1):
#     for j in range(1,i+2):
#         if j==1:
#             print(i,end="")
#         else:
#             print("*",end="")
#     print()








# # 66)

# # 0
# # *1
# # **2
# # ***3
# # ****4
# # *****5


# n = int(input("Enter a  number:"))

#  for i in range(0,n+1):
#     for j in range(0,i+1):
#         if j==i:
#             print(i,end="")
#         else:
#             print("*",end="")
#     print()







# # 67)


# # *****5
# # ****4
# # ***3
# # **2
# # *1
# # 0

# n = int(input("Enter a  number:"))

# for i in range(n,-1,-1):
#     for j in range(0,i+1):
#         if j==i:
#             print(i,end="")
#         else:
#             print("*",end="")
#     print()









# # 68)



# # *   *
# #  * * 
# #   *
# #  * *
# # *   *


# n = int(input("Enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==i or j == n-i+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# # 69)

# #   *  
# #   *  
# # *****
# #   *
# #   *

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 3 or j == 3:  
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()







# # 70)


# # *****
# # *   *
# # *   *
# # *   *
# # *****



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()







# # 71)


# # * * * * * 
# # * # # # *
# # * # # # *
# # * # # # *
# # * * * * *

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()





# # 72)


# # *******
# # **   **
# # * * * *
# # *  *  *
# # * * * *
# # **   **
# # *******



# n = 7
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or j == 1 or i == n or j == n or j == n-i+1  or i + j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()







# # 73)



# #  *
# #  **
# #  * *
# #  *  *
# #  *   *
# #  *    *
# #  *******



# n = int(input("enter a number:"))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == 1 or i == j or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()







# # 74)

# # *******
# # *    *
# # *   *
# # *  *
# # * *
# # **
# # *

# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1, n + 1):
#         if j == 1 or i == j or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()







# # 75)

# #       *
# #      **
# #     * *
# #    *  *
# #   *   *
# #  *    *
# # *******


# n = int(input("enter a number:"))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == n - i + 1 or j == n or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()







# # 76)


# # *******
# #  *    *
# #   *   *
# #    *  *
# #     * *
# #      **
# #       *

# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1, n + 1):
#         if j == n - i + 1 or j == n or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()





# # 77)

# #       *       
# #      * *      
# #     *   *
# #    *     *
# #   *       *
# #  *         *
# # *           *

# n = int(input("enter a number:"))


# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()






# # 78)





# # *           *
# #  *         *
# #   *       *
# #    *     *
# #     *   *
# #      * *
# #       *



# n = int(input("enter a number:"))


# for i in range(n-1,-1,-1):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()





# # 79)



# # *
# #  *
# #   *
# #    *
# #   *
# #  *
# # *


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j == i:
#             print("*",end="")
#         else:    
#             print(" ",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         if j == i:
#             print("*",end="")
#         else:    
#             print(" ",end="")
#     print()






# # 80)


# #    *
# #   *
# #  *
# # *
# #  *
# #   *
# #    *



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == n-i+1:
#             print("*",end="")
#         else:    
#             print(" ",end="")
#     print()
# for k in range(n-1,0,-1):
#     for l in range(1,n+1):
#         if l == n-k+1:
#             print("*",end="")
#         else:    
#             print(" ",end="")
#     print()







# # 81)




# #     *    
# #    * *   
# #   *   *
# #  *     *
# # *       *
# #  *     *
# #   *   *
# #    * *
# #     *


# n = int(input("enter a number:"))


# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()









# # 82)

# #      *
# #     / \
# #    /   \
# #   /     \
# #  /       \
# # /         \
# # \         /
# #  \       /
# #   \     /
# #    \   /
# #     \ /
# #      *


# n =int(input("Enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         if k == 1 and i == 1:
#             print("*",end="")
#         elif k == 1 :
#             print("/",end="")
#         elif k == 2*i-1:
#             print("\\",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         if k == 1 and i == 1:
#             print("*",end="")
#         elif k == 1 :
#             print("\\",end="")
#         elif k == 2*i-1:
#             print("/",end="")
#         else:
#             print(" ",end="")
#     print()










# # 83)



# #     *    
# #    - -   
# #   -   -
# #  -     -
# # -       -
# # -       -
# #  -     -
# #   -   -
# #    - -
# #     *

# n=int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         if i == 1 and k == 1:
#             print("*",end="")
#         elif k == 1 or k == 2*i-1:
#             print("-",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         if i == 1 and k == 1:
#             print("*",end="")
#         elif k == 1 or k == 2*i-1:
#             print("-",end="")
#         else:
#             print(" ",end="")
#     print()





# # 84)



# #    * 
# #   * * 
# #  * * *
# # * * * *
# #  * * *
# #   * *
# #    *

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()






# # 85)


# # *
# # **
# # ***
# # *
# # **
# # ***
# # *
# # **
# # ***



# n = 3
# for i in range(3):
#     for j in range(1, n+1):
#         print("*" * j)









# # 86)



# # *
# # **
# # ***
# # 1234
# # ***
# # **
# # *




# n = int (input("enter a number:"))
# x = 1
# for i in range(1,n+2):
#     for j in range(1,x+1):
#         if i!=n//2+1:
#             print("*",end="")
#         else:
#              print(j,end="")
#     print()
#     if i<=n//2:
#         x+=1
#     else:
#         x-=1






# # 87)


# # *
# # * *
# # ABC
# # * *
# # *


# n = int (input("enter a number:"))
# x = 1
# for i in range(1,n+2):
#     for j in range(1,x+1):
#         if i!=n//2+1:
#             print("*",end="")
#         else:
#              print(chr(64+j),end="")
#     print()
#     if i<=n//2:
#         x+=1
#     else:
#         x-=1







# # 88)


# # 1
# # 2* 2
# # 3* 3* 3
# # 4* 4* 4* 4
# # 3* 3* 3
# # 2* 2
# # 1

# n = int(input("enter a number:"))
# x = 1

# for i in range(1,n+1):
#     for j in range(1,x+1):
#         if j == x:
#             print(x,end=" ")
#         else:
#             print(str(x)+"*",end=" ")
#     print()
#     if i<=n//2:
#         x=x+1
#     else:
#         x=x-1





# # 89)

# # *******
# #  ***** 
# #   ***
# #    *
# #   ***
# #  *****
# # *******

# n = int(input("enter a number:"))
# for i in range(n,1,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()










# # 90)



# # *     *
# # **   **
# # *** ***
# # *******
# # *** ***
# # **   **
# # *     *


# n = int(input("Enter a number: "))
# for i in range(1, n):
#     for j in range(1, i+1):
#         print("*", end="")
#     for k in range(1, 2*(n-i)):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# for i in range(1, 2*n):
#     print("*", end="")
# print()

# for i in range(n-1, 0, -1):
#     for j in range(1, i+1):
#         print("*", end="")
#     for k in range(1, 2*(n-i)):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()


