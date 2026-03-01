
# # # 1)


# # Enter the row size for the pattern: 4
# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4 


# n= int (input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()





# # # 2))



#    1 2 3 4 5 
#    1 2 3 4
#    1 2 3
#    1 2
#    1

# n= int (input("enter a number:"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()








# # # 3))

# # Enter the row size for the pattern: 5
# #         1 
# #       1 2 1 
# #     1 2 3 2 1 
# #   1 2 3 4 3 2 1 
# # 1 2 3 4 5 4 3 2 1 



# n = int(input("enter a number:"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()











# # # 4))

# # 1 2 3 4 5 4 3 2 1
# #   1 2 3 4 3 2 1 
# #     1 2 3 2 1
# #       1 2 1
# #         1

# n = int(input("enter a number:"))


# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()









# # # 5))



# #            1 
# #          1 2 1
# #        1 2 3 2 1
# #      1 2 3 4 3 2 1
# #    1 2 3 4 5 4 3 2 1
# #      1 2 3 4 3 2 1
# #        1 2 3 2 1
# #          1 2 1
# #            1


# n = int(input("enter a number:"))



# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()







# # 6)

# # 1  
# # 1 0  
# # 1 0 1  
# # 1 0 1 0  
# # 1 0 1 0 1  


# n= int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()





# # 7)


# #     1  
# #    1 1  
# #   1 2 1  
# #  1 3 3 1  
# # 1 4 6 4 1  


# n = int(input("enter a number:"))

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if k == i :
#             print(1,end=" ")
#         else:
# #             print(k,end=" ")
# #     print()

# for i in range(5):
#     for j in range(5):
#         if i == 0 or j == 0 or i == 4 or j == 4:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




