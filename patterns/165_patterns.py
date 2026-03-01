# # 1)


# # *****
# # *****
# # *****
# # *****
# # *****



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="")
#     print()









# # 2)

# # *
# # **
# # ***
# # ****
# # *****


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()











# # 3)


# # *****
# # ****
# # ***
# # **
# # *



# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()












# # 4)

# #     *
# #    **
# #   ***
# #  ****
# # *****



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j  in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()












# # 5)



# # ******
# #  *****
# #   ****
# #    ***
# #     **
# #      *

# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()








# # 6)


# #    * 
# #   * * 
# #  * * *
# # * * * *



# n = int(input("enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()










# # 7)

# # * * * * * * 
# #  * * * * *
# #   * * * *
# #    * * *
# #     * *
# #      *

# n = int(input("enter a  number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()










# # 8)


# #      *
# #     ***
# #    *****
# #   *******
# #  *********


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i*2):
#         print("*",end="")
#     print()
    













# # 9)


# # ***********
# #  *********
# #   *******
# #    *****
# #     ***
# #      *

# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i*2):
#         print("*",end="")
#     print()










# # 10)


# # *
# # **
# # ***
# # ****
# # ***
# # **
# # *



# n = int(input("enter a  number:"))
# for i in range(1,n+2):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for k in range(n+2,0,-1):
#     for l in range(1,k+1):
#         print("*",end="")
#     print()









# # 11)


# #    *
# #   **
# #  ***
# # ****
# #  ***
# #   **
# #    *


# n = int(input("enter a  number:"))


# for i in range(1,n+2):
#     for j in range(1,n-i+2):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()
# for l in range(n,0,-1):
#     for m in range(1,n-l+2):
#         print(" ",end="")
#     for o in range(1,l+1):
#         print("*",end="")
#     print()










# # 12)



# # * * * * 1
# # * * * 2
# # * * 3
# # * 4
# # 5


# n = int(input("enter a  number:"))
# count = 1

# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         if j == n-i+1:
#             print(count,end="")
#             count = count + 1
#         else:
#             print("*",end=" ")
#     for k in range(1,i-1):
#         print(" ",end="")
#     print()









# # 13)


# # 1****
# # 22***
# # 333**
# # 4444*
# # 55555




# n = int(input("enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j <=i:
#             print(i,end="")
#         else:
#             print("*",end="")
#     print()





# # 14)


# # 1****
# # 12***
# # 123**
# # 1234*
# # 12345

# n = int(input("enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j <=i:
#             print(j,end="")
#         else:
#             print("*",end="")
#     print()







# # 15)


# # 55555
# # 4444*
# # 333**
# # 22***
# # 1****

# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in  range(1,n+1):
#         if j<=i:
#             print(i,end="")
#         else:
#             print("*",end="")
#     print()












# # 16)

# # 12345
# # 1234*
# # 123**
# # 12***
# # 1****



# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in  range(1,n+1):
#         if j<=i:
#             print(j,end="")
#         else:
#             print("*",end="")
#     print()







# # 17)

# # ****1
# # ***22
# # **333
# # *4444
# # 55555



# n = int(input("enter a  number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print("*",end="")
#     for k in range(i,0,-1):
#         print(k,end="")
#     print()








# # 18)

# # 55555
# # *4444
# # **333
# # ***22
# # ****1

 

# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i):
#         print("*",end="")
#     for k in range(i,n+1):
#         print(n-i+1,end="")
#     print()









# # 19)


# # 54321
# # *4321
# # **321
# # ***21
# # ****1


# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i):
#         print("*",end="")
#     for k in range(i,n+1):
#         print(n-k+1,end="")
#     print()








# # 20)


# # A****
# # BB***
# # CCC**
# # DDDD*
# # EEEEE



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(i+64),end="")
#     for k in range(i+1,n+1):
#         print("*",end="")

#     print()








# # 21)


# # A****
# # AB***
# # ABC**
# # ABCD*
# # ABCDE



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end="")
#     for k in range(i+1,n+1):
#         print("*",end="")

#     print()









# # 22)



# # EEEEE
# # DDDD*
# # CCC**
# # BB***
# # A****





# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(i+64),end="")
#     for k in range(1,n-i+1):
#         print("*",end="")
#     print()








# # 23)


# # ABCDE
# # ABCD*
# # ABC**
# # AB***
# # A****




# n = int(input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(j+64),end="")
#     for k in range(1,n-i+1):
#         print("*",end="")
#     print()






# # 24)


# # ****A
# # ***BB
# # **CCC
# # *DDDD
# # EEEEE



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print("*",end="")
#     for k in range(n-i+1,n+1):
#         print(chr(i+64),end="")
#     print()






# # 25)


# # ****A
# # ***BA
# # **CBA
# # *DCBA
# # EDCBA


# n= int(input("enter a number:"))

# for i in range(1,n+1):
#     count = i
#     for j in range(1,n-i+1):
#         print("*",end="")
#     for k in range(i,0,-1):
#         print(chr(k+64),end="")
#     print()







# # 26)


# # EEEEE
# # *DDDD
# # **CCC
# # ***BB
# # ****A


# n = int(input("enter a number:"))
# for i in range(n):
#     for j in range(i):
#         print("*",end="")
#     for k in range(n-i):
#         print(chr(n-i+64),end="")
#     print()










# # 27)


# # EDCBA
# # *DCBA
# # **CBA
# # ***BA
# # ****A





# n= int(input("enter a number:"))

# for i in range(n,0,-1):
#     count = i
#     for j in range(1,n-i+1):
#         print("*",end="")
#     for k in range(i,0,-1):
#         print(chr(k+64),end="")
#     print()











# # 28)


# # 1 2 3 4 *
# # 1 2 3 * 5
# # 1 2 * 4 5
# # 1 * 3 4 5
# # * 2 3 4 5



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == n-i+1:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#     print()







# # 29)


# # * 1 * 2 *
# # 3 * 4 * 5
# # * 6 * 7 *
# # 8 * 9 *10
# # * 11 * 12 *


# n = int(input("enter a number:"))

# count = 1

# for i in range(n):
#     for j in range(n):
#         if (i+j)%2==0:
#             print("*",end=" ")
#         else:
#             print(count,end=" ")
#             count = count + 1
#     print()








# # 30)


# # * A * B *
# # C * D * E
# # * F * G *
# # H * I * J
# # * K * L *





# n = int(input("enter a number:"))
# count = 0
# for i in range(n):
#     for j in range(n):
#         if (i+j)%2==0:
#             print("*",end=" ")
#         else:
#             print(chr(count + 65),end=" ")
#             count = count + 1
#     print()




    