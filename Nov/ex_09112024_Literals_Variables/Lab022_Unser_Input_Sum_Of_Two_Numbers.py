# write a program to take the 2 user input
# then sum number
# mul -> *
#dic -> /

#logic building
# step1
#I/P -> num1, num2 -> int  # DAA dont assume anything
#O/P -> sum -> int, dic -> float

num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
#intput always give to string type that why we have to convert

# num1 = int(num1)
# num2 = int(num2)

print(type(num1))
print(type(num2))

#Step 2 | Rough Logic
#Sum +, -, /, *

#str -> int
sum = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2

print("sum is ->", sum)
print("sub is ->", sub)
print("mul is ->", mul)
print("div is ->", div)

# num1 -> 155
# num2 -> 5
