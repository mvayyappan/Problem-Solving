a = 0
b = 1
sum = 0 
n = 10
temp = 0
for i in range(1,n+1):
    if a%2==0:
        sum = sum + 1
    temp = a
    a = b
    b = a + b
    print(sum)    
