# # 10


# # array sort 
# # binry search
# # anagram
# # rotate
# # common elemants




# board = [
# ['O','X','X'],
# ['X','X','O'],
# ['O','O','X']
# ]

# winner = None

# # check rows
# for i in range(3):
#     if board[i][0] == board[i][1] == board[i][2]:
#         winner = board[i][0]

# # check columns
# for j in range(3):
#     if board[0][j] == board[1][j] == board[2][j]:
#         winner = board[0][j]

# # check diagonals
# if board[0][0] == board[1][1] == board[2][2]:
#     winner = board[0][0]

# if board[0][2] == board[1][1] == board[2][0]:
#     winner = board[0][2]

# if winner:
#     print(winner, "wins")
# else:
#     print("Tie")


# def reverse_vowels(s):
#     vowels = "aeiouAEIOU"
#     s = list(s)  # convert string to list
#     # Step 1: collect all vowels in the string
#     vowel_list = []
#     for char in s:
#         if char in vowels:
#             vowel_list.append(char)
#     print(vowel_list)
#     print(s)
    
#     # Step 2: replace vowels in original string with reversed vowels
#     index = len(vowel_list) - 1  # start from last vowel
#     for i in range(len(s)):
#         if s[i] in vowels:
#             s[i] = vowel_list[index]
#             index -= 1
    
#     return "".join(s)

# # Test cases
# print(reverse_vowels("IceCreAm"))  # Output: "AceCreIm"
# print(reverse_vowels("aeiou"))     # Output: "uoiea"
# print(reverse_vowels("rhythm"))    # Output: "rhythm"



def num(n):

    if n<1:
        for i in range(2,n):
            if n%i==0:
                print("not")
        print("Prime")
    else:
        print("not")
    
num(8)
