# # 1. Find sum of all elements in a 2×2 matrix

# # Input:
# # 1 2
# # 3 4

# # Output:
# # 10


# mat1 = [[1,2],[3,4]]
# sum = 0
# for i in range(0,len(mat1)):
#     for j in range(len(mat1[i])):
#         sum = sum + mat1[i][j]
# print(sum)





    

# # 2. Find sum of each row in a 2×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6

# # Output:
# # Row 1 sum: 6
# # Row 2 sum: 15


# mat2 = [[1,2,3],
#        [4,5,6]]
# row_sum = 0
# for i in range(len(mat2)):
#     row_sum = 0
#     for j in range(len(mat2[i])):
#         row_sum = row_sum + mat2[i][j]
#     print("Row" , i+1 , "sum:" , row_sum)







# # 3. Find sum of each column in a 2×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6

# # Output:
# # Column 1 sum: 5
# # Column 2 sum: 7
# # Column 3 sum: 9


# mat3 = [[1,2,3],[4,5,6]]
# col_sum = 0
# for j in range(len(mat3[0])):
#     col_sum = 0
#     for i in range(len(mat3)):
#         col_sum = col_sum + mat3[i][j]
#     print("Column" ,  j+1 ,  "sum:", col_sum)






# # 4. Find max element in a 3×3 matrix

# # Input:
# # 5 8 3
# # 2 9 4
# # 7 1 6

# # Output:
# # Max element: 9



# mat4 = [[1,2,3],[14,5,6],[7,8,9]]
# max = mat4[0][0]
# for i in range(len(mat4)):
#     for j in range(len(mat4[i])):
#         if mat4[i][j]>max:
#             max = mat4[i][j]
# print("Max Element", max)







# # 5. Find min element in a 3×3 matrix

# # Input:
# # 5 8 3
# # 2 9 4
# # 7 1 6

# # Output:

# # Min element: 1

# mat5 = [[1,2,0],[14,5,6],[7,8,9]]
# min = mat5[0][0]
# for i in range(len(mat5)):
#     for j in range(len(mat5[i])):
#         if mat5[i][j]<min:
#             min = mat5[i][j]
# print("Min Element :", min)






# # 6. Transpose a 2×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6

# # Output:
# # 1 4
# # 2 5
# # 3 6




# mat6 = [[1,2,3],[4,5,6]]
# col = len(mat6[0])
# res = []
# for j in range(col):
#     curr = []
#     for i in range(len(mat6)):
#         curr.append(mat6[i][j])
#     res.append(curr)
# print(mat6)
# print(res)






# # 7. Multiply all elements by 2 in a 2×2 matrix

# # Input:
# # 1 2
# # 3 4

# # Output:
# # 2 4
# # 6 8



# mat7 = [[1, 2],[3, 4]]
# result = []
# for i in range(len(mat7)):
#     row = []
#     for j in range(len(mat7[i])):
#         row.append(mat7[i][j] * 2)
#     result.append(row)
# print(result)










# # 8. Check if a 2×2 matrix is symmetric

# # Input:
# # 1 2
# # 2 1

# # Output:
# # Symmetric


# mat8 = [ [1,2],[2,1]]
# if len(mat8) != len(mat8[0]):
#     print("Not Matrix")
# else:
#     symmetric = True
#     for i in range(0,len(mat8)):
#         for j in range(0,len(mat8[i])):
#             if mat8[i][j] != mat8[j][i]:
#                 symmetric = False
#     if symmetric:
#         print("Symmetric")
#     else:
#         print("Not Symmetric")
        









# # 9. Check if a 2×2 matrix is symmetric

# # Input:
# # 1 2
# # 3 4

# # Output:
# # Not symmetric


# mat9 = [ [1,2],[3,4]]
# if len(mat9) != len(mat9[0]):
#     print("Not Matrix")
# else:
#     symmetric = True
#     for i in range(0,len(mat9)):
#         for j in range(0,len(mat9[i])):
#             if mat9[i][j] != mat9[j][i]:
#                 symmetric = False
#     if symmetric:
#         print("Symmetric")
#     else:
#         print("Not Symmetric")
        








# # 10. Add two 2×2 matrices

# # Input:
# # Matrix A:
# # 1 2
# # 3 4

# # Matrix B:
# # 5 6
# # 7 8

# # Output:
# # 6 8
# # 10 12


# matA = [[1,2],[3,4]]
# matB = [[5,6],[7,8]]
# res = []
# curr = []
# for i in range(len(matA)):
#     curr = []
#     for j in range(len(matA[i])):
#         curr.append(matA[i][j] + matB[i][j])
#     res.append(curr)
# print(res)





# # 11. Subtract two 2×2 matrices

# # Input:
# # Matrix A:
# # 5 6
# # 7 8

# # Matrix B:
# # 1 2
# # 3 4

# # Output:
# # 4 4
# # 4 4

# matA = [[5,6],[7,8]]
# matB = [[1,2],[3,4]]
# res = []
# curr = []
# for i in range(len(matA)):
#     curr = []
#     for j in range(len(matA[i])):
#         curr.append(matA[i][j] - matB[i][j])
#     res.append(curr)
# print(res)






# # 12. Find row-wise maximum in 3×3 matrix

# # Input:
# # 1 2 3
# # 4 5 1
# # 7 2 6

# # Output:
# # Row 1 max: 3
# # Row 2 max: 5
# # Row 3 max: 7



# mat12 = [ [1,2,3] , [4,5,1] , [7,2,6] ]

# for i in range(len(mat12)):
#     max_row = mat12[i][0]
#     for j in range(len(mat12[i])):
#         if  mat12[i][j] > max_row:
#             max_row = mat12[i][j]
#     print("Max row element:",max_row)





# # 13. Find column-wise minimum in 3×3 matrix

# # Input:
# # 1 2 3
# # 4 5 1
# # 7 2 6

# # Output:
# # Col 1 min: 1
# # Col 2 min: 2
# # Col 3 min: 1


# mat13 = [[1,2,3],[4,5,6],[0,7,8]]
# col = len(mat13)
# for j in range(col):
#     col_min = mat13[0][j]
#     for i in range(len(mat13)):
#         if mat13[i][j]< col_min:
#             col_min = mat13[i][j]
#     print("Min Column element", col_min)






# # 14. Count even numbers in 3×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Output:
# # Even count: 4


# mat14 = [[1,2,3],[4,5,6],[7,8,9]]
# count = 0
# for i in range(len(mat14)):
#     for j in range(len(mat14[i])):
#         if mat14[i][j]%2==0:
#             count = count + 1
# print("Even count:" , count)






# # 15. Count odd numbers in 3×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Output:
# # Odd count: 5



# mat15 = [[1,2,3],[4,5,6],[7,8,9]]
# count = 0
# for i in range(len(mat15)):
#     for j in range(len(mat15[i])):
#         if mat15[i][j]%2==1:
#             count = count + 1
# print("Odd count:" , count)






# # 16. Find sum of diagonal elements in 3×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Output:
# # Diagonal sum: 15




# mat16 = [[1,2,3],[4,5,6],[7,8,9]]
# count = 0
# for i in range(len(mat16)):
#     count = count + mat16[i][i]
# print("Diagonal count:" , count)








# # 17. Find sum of anti-diagonal elements in 3×3 matrix

# # Input:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Output:
# # Anti-diagonal sum: 15


# mat17 = [[1,2,3],[4,5,6],[7,8,9]]
# count = 0
# n = len(mat17)
# for i in range(len(mat17)):
#     count = count + mat17[i][n-i-1]
# print("Diagonal count:" , count)







# # 18. Check if all elements are positive in 2×2 matrix

# # Input:
# # 1 2
# # 3 4

# # Output:
# # All positive



# mat18 = [[1,2],[3,4]]
# pos = True
# for i in range(len(mat18)):
#     for j in range(len(mat18[i])):
#         if mat18[i][j]<0:
#             pos = False

# if pos:
#     print("All positive")
# else:
#     print("False")





# # 19. Check if all elements are positive in 2×2 matrix

# # Input:
# # 1 -2
# # 3 4

# # Output:
# # Not all positive




# mat19 = [[1,-2],[3,4]]
# pos = True
# for i in range(len(mat19)):
#     for j in range(len(mat19[i])):
#         if mat19[i][j]<0:
#             pos = False

# if pos:
#     print("All positive")
# else:
#     print("Not All positive")






# # 20. Count zeros in 3×3 matrix

# # Input:
# # 0 1 2
# # 3 0 4
# # 5 6 0

# # Output:
# # Zero count: 3


# mat20 = [[0,1,2],[3,0,4],[5,6,0]]
# count = 0
# for i in range(len(mat20)):
#     for j in range(len(mat20[i])):
#         if mat20[i][j]==0:
#             count = count + 1
# print("Zero count:", count)







# # 21. Find the sum of two 3×3 matrices

# # Input:
# # Matrix A:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Matrix B:
# # 9 8 7
# # 6 5 4
# # 3 2 1

# # Output:
# # 10 10 10
# # 10 10 10
# # 10 10 10



# matA = [[1,2,3],[4,5,6],[7,8,9]]
# matB = [[9,8,7],[6,5,4],[3,2,1]]
# res = []
# for i in range(len(matA)):
#     curr = []
#     for j in range(len(matA)):
#         curr.append(matA[i][j] + matB[i][j])
#     res.append(curr)
# print(res)







# # 22. Subtract two 3×3 matrices

# # Input:
# # Matrix A:
# # 9 8 7
# # 6 5 4
# # 3 2 1

# # Matrix B:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Output:
# # 8 6 4
# # 2 0 -2
# # -4 -6 -8


# matA = [[9,8,7],[6,5,4],[3,2,1]]
# matB = [[1,2,3],[4,5,6],[7,8,9]]
# res = []
# for i in range(len(matA)):
#     curr = []
#     for j in range(len(matA)):
#         curr.append(matA[i][j] - matB[i][j])
#     res.append(curr)
# print(res)







# # 23. Multiply each element of a 3×3 matrix by 3

# # Input:
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # Output:
# # 3 6 9
# # 12 15 18
# # 21 24 27



# mat23 = [[1,2,3],[4,5,6],[7,8,9]]
# result = []
# for i in range(len(mat23)):
#     row = []
#     for j in range(len(mat23[i])):
#         row.append(mat23[i][j] * 3)
#     result.append(row)
# print(result)




# 24. Find sum of border elements in 3×3 matrix

# Input:

# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# Border sum: 40



# 25. Find sum of inner elements in 3×3 matrix

# Input:

# 1 2 3
# 4 5 6
# 7 8 9

# Output:

# Inner sum: 5
