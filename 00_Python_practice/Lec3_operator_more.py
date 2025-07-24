x = 15
y = 4
z = "Codenics"
a = "Python"

# addition
print("Addition:", x + y)  # 15 + 4 = 19

# subtraction
print("Subtraction:", x - y)  # 15 - 4 = 11

# multiplication
print("Multiplication:", x * y)  # 15 * 4 = 60

# division
print("Division:", x / y)  # 15 / 4 = 3.75

# print(x+z)   #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(z + a)  # This will concatenate the two strings "Codenics" and "Python"\
    
    
# comparison operators
print("Is x equal to y?", x == y)  # False, because 15 is not equal to 4
print("Is x not equal to y?", x != y)  # True, because 15 is not equal to 4
print("Is x greater than y?", x > y)  # True, because 15 is greater than 4  
print("Is x less than y?", x < y)  # False, because 15 is not less than 4   
print("Is x greater than or equal to y?", x >= y)  # True, because 15 is greater than 4
print("Is x less than or equal to y?", x <= y)  # False, because 15 is not less than or equal to 4


# logical operators
print("Is x greater than 10 and y less than 5?", x > 10 and y < 5)  # True, because both conditions are true
print("Is x less than 10 or y greater than 5?", x < 10 or y > 5)  # False, because both conditions are false
print("Is not x greater than 10?", not (x > 10))  # False, because x is greater than 10

# identity operators
print("Is x identical to y?", x is y)  # False, because x and y are not the same object
print("Is x not identical to y?", x is not y)  # True, because x and y are not the same object

# membership operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 a member of my_list?", 3 in my_list)  # True, because 3 is in the list
print("Is 6 not a member of my_list?", 6 not in my_list)  # True, because 6 is not in the list

# bitwise operators
print("Bitwise AND of x and y:", x & y)  # Bitwise AND operation
print("Bitwise OR of x and y:", x | y)  # Bitwise OR operation
print("Bitwise XOR of x and y:", x ^ y)  # Bitwise XOR operation
print("Bitwise NOT of x:", ~x)  # Bitwise NOT operation
print("Left shift x by 2:", x << 2)  # Left shift operation
print("Right shift x by 2:", x >> 2)  # Right shift operation


# assignment operators
x += 5  # Equivalent to x = x + 5
print("After adding 5, x is now:", x)  # x is now 20
y -= 2  # Equivalent to y = y - 2
print("After subtracting 2, y is now:", y)  # y is now 2
z *= 2  # Equivalent to z = z * 2
print("After multiplying by 2, z is now:", z)  # z is now "CodenicsCodenics"
a /= 2  # Equivalent to a = a / 2
print("After dividing by 2, a is now:", a)  # a is now "Python" (string division not applicable)


# floor division
print("Floor division of x by y:", x // y)  # Floor division, result is 10

# modulus
print("Modulus of x by y:", x % y)  # Modulus operation, result is 0

# exponentiation
print("Exponentiation of x to the power of y:", x ** y)  # Exponentiation, result is 100000

# ternary operator
result = "x is greater than y" if x > y else "x is not greater than y"

print("Ternary operator result:", result)  # This will print "x is greater than y" since x is now 20 and y is 2

# type casting
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print("Type casting string '123' to integer:", num_int)  # This will print 123

# type checking
print("Type of x:", type(x))  # This will print <class 'int'>
print("Type of z:", type(z))  # This will print <class 'str'>, since z is a string
# type conversion
num_float = float(num_int)  # Convert integer to float
print("Type conversion of integer to float:", num_float)  # This will print 123.0
# type checking after conversion
print("Type of num_float:", type(num_float))  # This will print <class 'float'>
# type checking for string
print("Type of z after concatenation:", type(z))  # This will print <class 'str'>, since z is still a string
