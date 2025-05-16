#Write a script that takes two numbers as input and prints whether
#the first number is greater than, less than, or equal to the second
#number.

a=int(input("Enter the first Number :"))
b=int(input("Enter the second  Number :"))

if a>b:
    print(f"The number {a} is greater than {b}")
elif a<b:
    print(f"The number {b} is greater than {a}")
else:
    print("The Numbers are equal.")
