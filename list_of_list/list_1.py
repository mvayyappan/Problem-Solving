# # 1)) sum list


# def sum_list(l):
#     sum = 0
#     for i in range(len(l)):
#         sum = sum + l[i]
#     print(sum)

# sum_list([1,2,3,4,5])








# # 2)) sum list positive num

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










# # 9) multiple_items in list but without using loop


# def product(lst):
#     if len(lst) == 1:        
#         return lst[0]
#     return lst[0] * product(lst[1:])

# numbers = [2, 3, 4, 5]
# print(product(numbers))








# # 10)

# def cumulative_product(l):
#     mul = 1
#     lst = []
#     for i in range(0,len(l),+1):
#         mul = mul * l[i]
#         lst.append(mul)
#     print(lst)
# cumulative_product([1,2,3,4])









# # 11) maximum number


# def max(l):
#     max = l[0]
#     for i in l:
#         if i>max:
#             max = i
#     print(max)
# max([1,2,3,4,5])

    








# # 12) second maximum number

# def second_max(l):
#     if len(l) == 1:
#         print("not a second max")
#     else:
#         max = l[0]
#         for i in l:
#             if i>max:
#                 max = i
#         sec_max=l[0]
#         for j in l:
#             if j>sec_max and max!=j:
#                 sec_max=j
#         print(sec_max)
# second_max([1,2,3,4]) 
        








# # 13)  maximum number multiple of 5



# def max(l):
#     max = l[0]
#     for i in l:
#         if i>max and i%5==0:
#             max = i
#     print(max)
# max([1,2,13,10,5])










# # 14)  unique maximum number

# def unique_max(l):
#     count = {}
#     if len(l) == 0:
#         print("invalid")
#     elif len(l) == 1:
#         print(l[0])
#     else:
#         for i in range(0,len(l),+1):
#             if l[i] in count:
#                 count[l[i]] += 1
#             else:
#                 count[l[i]] = 1
#     found = 0
#     result = -999999999   
#     for key in count:
#         if count[key] == 1:
#             if found == 0:
#                 result = key
#                 found = 1
#             else:
#                 if key>result:
#                     result = key
#     if found == 0:
#         print("no unique number")
#     else:
#         print("unique max number:", result)
        
# unique_max([1,2,3,4,5,5,4,3,2])









# # 15)  maximum even number 



# def max(l):
#     max = l[0]
#     for i in l:
#         if i>max and i%2==0:
#             max = i
#     print(max)
# max([1,2,13,10,5])






# # 16)  minimum  number 



# def min(l):
#     min = l[0]
#     for i in l:
#         if i<min:
#             min = i
#     print(min)
# min([1,2,13,10,5])










# # 17) second minimum number


# def sec_min(l):
#     min = l[0]
#     for i in l:
#         if i<min:
#             min = i
#     sec_min = l[-1]
#     for j in l:
#         if j<=sec_min and min!=j:
#             sec_min=j
#     print(sec_min)


# sec_min([1,2,3,4,5,6])








# # 18) minimum prime number


# def prime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True

# def min_prime(l):
#     minimum = None
#     for n in l:
#         if prime(n):          
#             if minimum is None or n < minimum:
#                 minimum = n

#     if minimum is None:
#         print("No prime numbers")
#     else:
#         print("Minimum prime:", minimum)

# min_prime([1,4,6,8,9,10])








# # 19)  Count Strings with Same Start and End

# def same_start_and_end(arr):
#     if len(arr) == 0:
#         print("invalid input")
#     else:
#         count = 0
#         for i in range(0,len(arr),+1):
#             if arr[i][0] == arr[i][-1]:
#                 count = count + 1 
#         print(count)
        
# same_start_and_end(["121","aba","123451"])





# 20)count  palindrome


def palindrome(a):
    if len(a) == 0:
        print("invalid")
    else:
        for i in range(0,len(a),+1):
            if a[i] != a[len(a)-1-i]:
                print(False)
                break
            print(True)
palindrome("123")
        




