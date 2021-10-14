#Implicit function 

number_integer = 123
number_float = 123.45

sum = number_integer + number_float

print(sum)

#Type() function

number_integer = 123
number_float = 123.45

sum = number_integer + number_float

print("The datatype of sum:", type(sum))

# Explicit type conversion

float_number = 1.2345

integer_number = int(float_number)
print(type(integer_number))
print(integer_number)

# Converting string to int and float

a = '55'

integer_number = int(a)
float_number = float(a)

print("Integer Number is:\t", integer_number)
print("Float Number is:\t", float_number)

# int and float to string 

a = 34.56
b = 45.76

str_a = str(a)
str_b = str(b)

print(str_a)
print(type(str_a))

print(str_b)
print(type(str_b))

# Error during type conversion

a = 'hello'
integer_number = int(a)

# Error during type conversion(part 2)

a = '55.7'
b = float(a)

print(b)
# Output: 55.7

a = '44.6'
b = int(a)
# Output: ValueError: invalid literal for int() with base 10: '44.6'


# Loss of information during conversion

float_number = 34.67
integer_number = int(float_number)

print("float number:\t", float_number)
print("integer number:\t", integer_number)

