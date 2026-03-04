# # 1. Create a dictionary

# # Input: name = "Ram", age = 18
# # Output: {'name': 'Ram', 'age': 18}


# a = {"name" : "Ram", "age": 18}
# print(a)




# # 2. Print value using key

# # Input: {'a':10, 'b':20}, key = 'a'
# # Output: 10


# a = {"name" : "Ram", "age": 18}
# print(a["name"])






# # 3. Add new key

# # Input: {'a':1}, add b:2
# # Output: {'a':1, 'b':2}

# a = {"name" : "Ram", "age": 18}
# a["native"] = "paramakudi"
# print(a)






# # 4. Update value

# # Input: {'a':5}, update a to 10
# # Output: {'a':10}

# a = {'name': 'Ram', 'age': 18, 'native': 'paramakudi'}
# a["native"] = "Ramanathapuram"
# print(a)






# # 5. Delete key

# # Input: {'a':1, 'b':2}, delete 'a'
# # Output: {'b':2}



# a = {'name': 'Ram', 'age': 18, 'native': 'paramakudi'}
# del a["native"]
# print(a)






# 6. Check key exists

# Input: {'x':100}, key = 'x'
# Output: True






# 7. Length of dictionary

# Input: {'a':1, 'b':2, 'c':3}
# Output: 3

# 8. Get all keys

# Input: {'a':1, 'b':2}
# Output: ['a','b']

# 9. Get all values

# Input: {'a':1, 'b':2}
# Output: [1,2]

# 10. Clear dictionary

# Input: {'a':1, 'b':2}
# Output: {}

# 11. Loop and print keys

# Input: {'a':1, 'b':2}
# Output:
# a
# b

# 12. Loop and print values

# Input: {'a':1, 'b':2}
# Output:
# 1
# 2

# 13. Simple frequency count

# Input: "aa"
# Output: {'a':2}

# 14. Count numbers

# Input: [1,1,2]
# Output: {1:2, 2:1}

# 15. Square numbers

# Input: [2,3]
# Output: {2:4, 3:9}

# 16. Merge two dict

# Input: {1:1}, {2:2}
# Output: {1:1, 2:2}

# 17. Print only keys

# Input: {'a':10}
# Output: a

# 18. Print only values

# Input: {'a':10}
# Output: 10

# 19. Replace value

# Input: {'a':5}
# Output after change to 7: {'a':7}

# 20. Dictionary from list

# Input: ['a','b']
# Output: {'a':1, 'b':1}

# 21. Dictionary from two lists

# Input: keys = [1,2], values = [10,20]
# Output: {1:10, 2:20}

# 22. Find max value

# Input: {'a':5, 'b':10}
# Output: 10

# 23. Find min value

# Input: {'a':5, 'b':10}
# Output: 5

# 24. Check empty

# Input: {}
# Output: True

# 25. Remove using pop

# Input: {'a':1, 'b':2}, pop 'b'
# Output: {'a':1}

# 26. Convert dict to list

# Input: {'a':1}
# Output: [('a',1)]

# 27. Access using get()

# Input: {'a':5}, get 'a'
# Output: 5

# 28. Get missing key with default

# Input: {'a':5}, get 'b' with default 0
# Output: 0

# 29. Update multiple values

# Input: {'a':1}, update with {'b':2}
# Output: {'a':1, 'b':2}

# 30. Copy dictionary

# Input: {'a':1}
# Output: {'a':1}






# 1. Count frequency of each character

# Input: "apple"
# Output: {'a':1, 'p':2, 'l':1, 'e':1}








# 2. Count frequency of each word

# Input: "this is is test"
# Output: {'this':1, 'is':2, 'test':1}







# 3. First non-repeating character

# Input: "aabbcde"
# Output: 'c'







# 4. Find duplicate characters

# Input: "programming"
# Output: {'r':2, 'g':2, 'm':2}








# 5. Element and its square

# Input: [1,2,3,4]
# Output: {1:1, 2:4, 3:9, 4:16}











# 6. Count numbers in list

# Input: [1,2,2,3,1,4]
# Output: {1:2, 2:2, 3:1, 4:1}











# 7. Merge two dictionaries

# Input:
# d1 = {1:10, 2:20}
# d2 = {3:30, 4:40}
# Output: {1:10, 2:20, 3:30, 4:40}











# 8. Key with maximum value

# Input: {'a':10, 'b':25, 'c':15}
# Output: 'b'










# 9. Key with minimum value

# Input: {'a':10, 'b':25, 'c':5}
# Output: 'c'











# 10. Invert dictionary

# Input: {'a':1, 'b':2}
# Output: {1:'a', 2:'b'}










# 11. Group even and odd

# Input: [1,2,3,4,5]
# Output: {'even':[2,4], 'odd':[1,3,5]}










# 12. Students above 75

# Input: {'ram':80, 'sam':60, 'raj':90}
# Output: ['ram','raj']










# 13. Count vowels

# Input: "education"
# Output: {'e':1, 'u':1, 'a':1, 'i':1, 'o':1}










# 14. Names and lengths

# Input: ['ram','kumar','raj']
# Output: {'ram':3, 'kumar':5, 'raj':3}










# 15. Anagram check

# Input: "listen", "silent"
# Output: True










# 16. Most frequent element

# Input: [1,2,2,3,3,3]
# Output: 3










# 17. Numbers 1 to N cube

# Input: N = 3
# Output: {1:1, 2:8, 3:27}










# 18. Remove value < 50

# Input: {'a':60, 'b':40, 'c':80}
# Output: {'a':60, 'c':80}










# 19. Common keys

# Input:
# d1 = {'a':1, 'b':2}
# d2 = {'b':3, 'c':4}
# Output: {'b'}










# 20. Sum duplicate keys

# Input: [(1,10),(2,20),(1,15)]
# Output: {1:25, 2:20}