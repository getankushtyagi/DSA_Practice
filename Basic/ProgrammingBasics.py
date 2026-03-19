"""
================================================================================
              PROGRAMMING BASICS - COMPLETE LEARNING GUIDE
================================================================================

FUNDAMENTAL CONCEPTS FOR PROBLEM SOLVING
-----------------------------------------
This guide covers essential programming concepts and patterns that form the
foundation of algorithmic problem solving.


================================================================================
                        1. VARIABLES & DATA TYPES
================================================================================

PRIMITIVE DATA TYPES:

1. INTEGERS (int)
   - Whole numbers: -2, -1, 0, 1, 2, 100
   - Operations: +, -, *, //, %, **
   
   x = 10
   y = -5
   result = x + y  # 5

2. FLOATING POINT (float)
   - Decimal numbers: 3.14, -0.5, 2.0
   - Operations: +, -, *, /, **
   
   pi = 3.14159
   radius = 2.5
   area = pi * radius ** 2

3. BOOLEAN (bool)
   - True or False
   - Used in conditions and logic
   
   is_valid = True
   is_empty = False

4. STRINGS (str)
   - Text data: \"Hello\", 'World'
   - Immutable sequence of characters
   
   name = \"Alice\"
   greeting = 'Hello, ' + name

5. NONE
   - Represents absence of value
   - Similar to null in other languages
   
   result = None


================================================================================
                        2. OPERATORS
================================================================================

ARITHMETIC OPERATORS:
   +   Addition
   -   Subtraction
   *   Multiplication
   /   Division (float result)
   //  Integer division
   %   Modulo (remainder)
   **  Exponentiation

Examples:
   10 + 3  = 13
   10 - 3  = 7
   10 * 3  = 30
   10 / 3  = 3.333...
   10 // 3 = 3
   10 % 3  = 1
   10 ** 3 = 1000

COMPARISON OPERATORS:
   ==  Equal to
   !=  Not equal to
   >   Greater than
   <   Less than
   >=  Greater than or equal
   <=  Less than or equal

Examples:
   5 == 5  → True
   5 != 3  → True
   5 > 3   → True
   5 < 3   → False

LOGICAL OPERATORS:
   and  Both conditions true
   or   At least one condition true
   not  Negation

Examples:
   True and False  → False
   True or False   → True
   not True        → False

BITWISE OPERATORS:
   &   AND
   |   OR
   ^   XOR
   ~   NOT
   <<  Left shift
   >>  Right shift

Examples:
   5 & 3   = 1   (0101 & 0011 = 0001)
   5 | 3   = 7   (0101 | 0011 = 0111)
   5 ^ 3   = 6   (0101 ^ 0011 = 0110)
   5 << 1  = 10  (0101 << 1 = 1010)


================================================================================
                        3. CONTROL STRUCTURES
================================================================================

IF-ELSE STATEMENTS:

   if condition:
       # code if condition is True
   elif another_condition:
       # code if another_condition is True
   else:
       # code if all conditions are False

Example:
   age = 18
   if age < 18:
       print(\"Minor\")
   elif age == 18:
       print(\"Just turned adult\")
   else:
       print(\"Adult\")

FOR LOOPS:

   # Iterate over range
   for i in range(5):
       print(i)  # 0, 1, 2, 3, 4
   
   # Iterate over list
   fruits = [\"apple\", \"banana\", \"cherry\"]
   for fruit in fruits:
       print(fruit)
   
   # With index
   for i, fruit in enumerate(fruits):
       print(f\"{i}: {fruit}\")

WHILE LOOPS:

   count = 0
   while count < 5:
       print(count)
       count += 1
   
   # Infinite loop with break
   while True:
       user_input = input(\"Enter 'q' to quit: \")
       if user_input == 'q':
           break

LOOP CONTROL:
   break    - Exit loop
   continue - Skip to next iteration
   pass     - Do nothing (placeholder)


================================================================================
                        4. FUNCTIONS
================================================================================

FUNCTION DEFINITION:

   def function_name(parameters):
       \"\"\"Docstring describing function\"\"\"
       # function body
       return result

Examples:

   # Simple function
   def greet(name):
       return f\"Hello, {name}!\"
   
   # Multiple parameters
   def add(a, b):
       return a + b
   
   # Default parameters
   def power(base, exponent=2):
       return base ** exponent
   
   # Variable number of arguments
   def sum_all(*args):
       return sum(args)
   
   # Keyword arguments
   def describe_person(**kwargs):
       for key, value in kwargs.items():
           print(f\"{key}: {value}\")

LAMBDA FUNCTIONS:
   Small anonymous functions

   square = lambda x: x ** 2
   add = lambda x, y: x + y
   
   # Used with map, filter
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x**2, numbers))


================================================================================
                        5. COMMON PATTERNS
================================================================================

1. SWAP TWO VARIABLES
   a, b = b, a

2. FIND MIN/MAX
   min_val = min(a, b, c)
   max_val = max(a, b, c)

3. ABSOLUTE VALUE
   abs_val = abs(-5)  # 5

4. ROUNDING
   round(3.7)      → 4
   round(3.14, 1)  → 3.1
   int(3.9)        → 3  (truncate)

5. CHECK EVEN/ODD
   if num % 2 == 0:
       print(\"Even\")
   else:
       print(\"Odd\")

6. FACTORIAL
   def factorial(n):
       if n <= 1:
           return 1
       return n * factorial(n - 1)

7. FIBONACCI
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n-1) + fibonacci(n-2)

8. PRIME NUMBER CHECK
   def is_prime(n):
       if n < 2:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True

9. PALINDROME CHECK
   def is_palindrome(s):
       return s == s[::-1]

10. ANAGRAM CHECK
    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)


================================================================================
                        6. STRING MANIPULATION
================================================================================

COMMON OPERATIONS:

   s = \"Hello World\"
   
   # Length
   len(s)  # 11
   
   # Access by index
   s[0]    # 'H'
   s[-1]   # 'd'
   
   # Slicing
   s[0:5]  # 'Hello'
   s[:5]   # 'Hello'
   s[6:]   # 'World'
   s[::-1] # 'dlroW olleH' (reverse)
   
   # Methods
   s.lower()           # 'hello world'
   s.upper()           # 'HELLO WORLD'
   s.replace('o', 'a') # 'Hella Warld'
   s.split()           # ['Hello', 'World']
   s.strip()           # Remove whitespace
   s.startswith('H')   # True
   s.endswith('d')     # True
   s.find('Wor')       # 6 (index)
   s.count('l')        # 3

STRING FORMATTING:

   name = \"Alice\"
   age = 25
   
   # f-strings (Python 3.6+)
   f\"Name: {name}, Age: {age}\"
   
   # format() method
   \"Name: {}, Age: {}\".format(name, age)
   
   # % formatting
   \"Name: %s, Age: %d\" % (name, age)


================================================================================
                        7. LIST OPERATIONS
================================================================================

CREATION:
   arr = [1, 2, 3, 4, 5]
   arr = list(range(1, 6))
   arr = [0] * 5  # [0, 0, 0, 0, 0]

COMMON OPERATIONS:
   arr.append(6)        # Add to end
   arr.insert(0, 0)     # Insert at index
   arr.pop()            # Remove last
   arr.pop(0)           # Remove at index
   arr.remove(3)        # Remove first occurrence
   arr.reverse()        # Reverse in-place
   arr.sort()           # Sort in-place
   sorted(arr)          # Return sorted copy
   arr.count(2)         # Count occurrences
   arr.index(3)         # Find index
   arr.clear()          # Remove all

LIST COMPREHENSION:
   # Create list
   squares = [x**2 for x in range(10)]
   
   # With condition
   evens = [x for x in range(10) if x % 2 == 0]
   
   # Nested
   matrix = [[i*j for j in range(3)] for i in range(3)]


================================================================================
                        8. MATHEMATICAL CONCEPTS
================================================================================

COMMON FORMULAS:

1. Sum of first n natural numbers:
   sum = n * (n + 1) // 2

2. Sum of squares:
   sum = n * (n + 1) * (2*n + 1) // 6

3. Sum of cubes:
   sum = (n * (n + 1) // 2) ** 2

4. GCD (Greatest Common Divisor):
   def gcd(a, b):
       while b:
           a, b = b, a % b
       return a

5. LCM (Least Common Multiple):
   lcm = (a * b) // gcd(a, b)

6. Check if power of 2:
   is_power_of_2 = (n > 0) and (n & (n - 1) == 0)

7. Count set bits:
   count = bin(n).count('1')


================================================================================
                        9. INPUT/OUTPUT
================================================================================

INPUT:
   # String input
   name = input(\"Enter name: \")
   
   # Integer input
   num = int(input(\"Enter number: \"))
   
   # Multiple inputs
   a, b = input().split()
   a, b = map(int, input().split())
   
   # List input
   arr = list(map(int, input().split()))

OUTPUT:
   print(\"Hello\")
   print(\"Value:\", 42)
   print(f\"Name: {name}\")
   print(\"Line 1\", end=\" \")  # No newline
   print(\"Line 2\", sep=\"-\")   # Custom separator


================================================================================
                        10. ERROR HANDLING
================================================================================

TRY-EXCEPT:
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print(\"Cannot divide by zero\")
   except Exception as e:
       print(f\"Error: {e}\")
   finally:
       print(\"Always executed\")


================================================================================
                        11. COMMON ALGORITHMS
================================================================================

1. LINEAR SEARCH:
   def linear_search(arr, target):
       for i, val in enumerate(arr):
           if val == target:
               return i
       return -1

2. BINARY SEARCH:
   def binary_search(arr, target):
       left, right = 0, len(arr) - 1
       while left <= right:
           mid = (left + right) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       return -1

3. REVERSE ARRAY:
   def reverse(arr):
       left, right = 0, len(arr) - 1
       while left < right:
           arr[left], arr[right] = arr[right], arr[left]
           left += 1
           right -= 1


================================================================================
                        PRACTICE PROBLEMS
================================================================================

BEGINNER:
1. Hello World
2. Sum of two numbers
3. Even or odd
4. Factorial
5. Fibonacci
6. Palindrome check
7. Prime number
8. Armstrong number
9. Swap two numbers
10. Reverse a number

INTERMEDIATE:
1. GCD and LCM
2. Binary to decimal
3. Sum of digits
4. Count vowels and consonants
5. Remove duplicates
6. Find second largest
7. Check anagram
8. Power without using **
9. Perfect number check
10. String rotation

================================================================================
"""
