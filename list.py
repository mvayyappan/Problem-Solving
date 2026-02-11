# # 1)) sum list


# def sum_list(l):
#     sum = 0
#     for i in range(len(l)):
#         sum = sum + l[i]
#     print(sum)

# sum_list([1,2,3,4,5])







# # 2)) sum list +num

# def sum_list_positive_numbers(l):
#     sum = 0
#     for i in range(len(l)):
#         if l[i] >=0:
#             sum = sum + l[i]
#     print(sum)
# sum_list_positive_numbers([-1,-2,-3,-4,-5,1,2,3,4,5])






# # 3)) sum list multiple of 3


# def sum_list_multiple_of_3(l):
#     sum = 0
#     for i in range(len(l)):
#         if l[i]%3==0:
#             sum = sum + l[i]
#     print(sum)
# sum_list_multiple_of_3([1,2,3,4,5,6,7,8,9,0])








# # 4))  sum a nested list

# def sum_nested_list(l):
#     sum = 0
#     for i in range(len(l)):
#         for j in range(len(l[i])):
#             sum = sum + l[i][j]
#     print(sum)
# sum_nested_list([[1,2,3],[4,5,6],[7,8,9],[10]])








# # 5))  sum of digit in each element 


# def sum_of_digit_in_each_element_in_list(l):
#     result = []
#     sum = 0
#     for n in l:
#         sum = 0
#         while n>0:
#             digit = n%10
#             sum = sum + digit
#             n = n//10
#         result.append(sum)
#     print(result)
# sum_of_digit_in_each_element_in_list([123,456,789,0])





# # 6) multiple of all items im list


# def multiple_list(l):
#     mul = 1
#     for i in range(len(l)):
#         mul = mul*l[i]
#     print(mul)
# multiple_list([1,2,3,4,5])







# # 7) multiple of odd numbers

# def multiple_odd(l):
#     mul = 1
#     for i in range(len(l)):
#         if l[i]%2==1:mul = mul * l[i]
#     print(mul)
# multiple_odd([1,2,3,4,5])









# # 8) multiple of items ignore zero

# def multiple_items_ignore_zero(l):
#     multi = 1
#     for i in range(len(l)):
#         if l[i] != 0:
#             multi = multi*l[i]
#     print(multi)
# multiple_items_ignore_zero([1,2,3,4,5,0])








# 9) multiple_items in list but without using loop


def multiple_items_ignore_loop(l):
    sum = 0
    count = 0
    sum  = sum + l[count]
    count = count + 1
    

        




















