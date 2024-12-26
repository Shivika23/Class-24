num = int(input("Enter a number"))
result = 0
temp = num

while temp!=0:
    digit = num%10
    result = result + digit**3
    temp = temp//10

print(result)
if result == num:
    print("is armstrong")
else:
    print("is not armstrong")
    


