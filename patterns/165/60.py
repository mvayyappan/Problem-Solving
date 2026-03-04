
# # 31)

# # * # # # # # #
# # # # # # # * *
# # * * * # # # #
# # # # # * * * *
# # * * * # # # #
# # # # # # # * *
# # * # # # # # #




# n = int(input("enter a number:"))

# count = 1

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%2==1 and j<=count:
#             print("*",end=" ")
#         elif i%2==0 and n-j+1<=count:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()
#     if i<=n//2:
#         count+=1
#     else:
#         count-=1






# # 32)

# # * 0 0 0 * 0 0 0 *
# # 0 * 0 0 * 0 0 * 0
# # 0 0 * 0 * 0 * 0 0
# # 0 0 0 * * * 0 0 0
# # 0 0 0 0 * 0 0 0 0



# n = int(input("enter a number:"))
# for i in range(1, n + 1):
#     for j in range(1, 2 * n):
#         if j == i or j == 2 * n - i or j == n:
#             print("* ", end="")
#         else:
#             print("0 ", end="")
#     print()






# # 33)

# # 1
# # 1* 2
# # 1* 2* 3
# # 1* 2* 3* 4
# # 1* 2* 3* 4* 5

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i <= j:
#             print(str(j),end=" ")
#         else:
#             print(str(j)+"*",end=" ")
#     print()






# # 34)


# # 1 
# # 2* 3
# # 4* 5* 6
# # 7* 8* 9* 10
# # 11* 12* 13* 14* 15


# n = int(input("enter a number:"))
# count = 0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         count = count + 1
#         if i <= j:
#             print(str(count),end=" ")
#         else:
#             print(str(count)+"*",end=" ")
#     print() 






# # 35)


# # #
# # **
# # ###
# # ****
# # #####


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print("#",end="")
#     print()




# # 36)


# # 1
# # **
# # 333
# # ****
# # 55555


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print(i,end="")
#     print()





# # 37)


# 1
# **
# 123
# ****
# 12345






# 38)

# 1
# 1*
# 1*3
# 1*3*
# 1*3*5







# 39)




# # 1
# # 2*
# # 3*3
# # 4*4*
# # 5*5*5





# n = int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("*",end="")
#         else:
#             print(i,end="")
#     print()





# # 40


# # #####
# # ****
# # ###
# # **
# # #


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print("#",end="")
#     print()




# # 41)

# # #*#*#
# # #*#*
# # #*#
# # #*
# # #


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("*",end="")
#         else:
#             print("#",end="")
#     print()






# # 42)


# # 55555
# # ****
# # 333
# # **
# # 1


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print(i,end="")
#     print()







# # 43)


# # 12345
# # ****
# # 123
# # **
# # 1


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print(j,end="")
#     print()







# # 44)


# 1*3*5
# 1*3*
# 1*3
# 1*
# 1



# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("*",end="")
#         else:
#             print(j,end="")
#     print()











# 45)

# # 1*3*5
# # 1*3*
# # 1*3
# # 1*
# # 1


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("*",end="")
#         else:
#             print(j,end="")
#     print()












# # 46)


# #     #
# #    * *
# #   # # #
# #  * * * *
# # # # # # #

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()









# # 47)


# #     #
# #    * #
# #   # * #
# #  * # * #
# # # * # * #


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()











# # 48)

# #     1
# #    * *
# #   3 3 3
# #  * * * *
# # 5 5 5 5 5 



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#     print()









# # 49)


# #     1
# #    * *
# #   3 2 1
# #  * * * *
# # 5 4 3 2 1



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(k,end=" ")
#     print()










# # 50)


# #     5
# #    * *
# #   3 4 5
# #  * * * *
# # 1 2 3 4 5


# n = int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(n-k+1,end=" ")
#     print()








# # 51)



# #     1
# #    * 1
# #   3 * 1
# #  * 3 * 1
# # 5 * 3 * 1

 
# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print(k,end=" ")
#     print()








# # 52)

# #     1
# #    * 2
# #   3 * 3
# #  * 4 * 4
# # 5 * 5 * 5


 
# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#     print()






# # 53)


# #  # # # # #
# #   * * * *
# #    # # #
# #     * *
# #      *


# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()








# # 54)

# # # * # * #
# #  * # * #
# #   # * #
# #    * #
# #     #

# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()








# # 55)

# # 5 5 5 5 5
# #  * * * *
# #   3 3 3
# #    * *
# #     1


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#     print()






# # 56)


# # 5 4 3 2 1
# #  * * * *
# #   3 2 1
# #    * *
# #     1


# n = int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(k,end=" ")
#     print()





# # 57)


# # 5 * 3 * 1
# #  * 3 * 1 
# #   3 * 1 
# #    * 1
# #     1


# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print(k,end=" ")
#     print()
    



# # 58)


# #     #
# #    * *
# #   # # #
# #  * * * *
# # # # # # #


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")       
#     print()







# # 59)


# #     #
# #    * #
# #   # * #
# #  * # * #


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()




# # 60)


# #     1
# #    * *
# #   3 3 3
# #  * * * *
# # 5 5 5 5 5



# from tkinter import E


# n = int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#     print()






