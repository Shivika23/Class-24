
def roman_to_int(a):
    if a == "I":
        print(1)
    
    if a == "V":
        print(5)

    if a == "X":
        print(10)

    if a == "L":
        print(50)

    if a == "C":
        print(100)

    if a == "D":
        print(500)

    if a== "M":
        print(1000)

a = input("Please enter a Roman Numeral: ")
print("Integer form of " + a + " is:")
print(roman_to_int(a))