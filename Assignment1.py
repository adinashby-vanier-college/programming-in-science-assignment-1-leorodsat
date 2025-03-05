# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    return(max(num1, num2, num3))

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return(min(num1, num2, num3))

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        return("Positive")
    elif number < 0:
        return("Negative")
    else:
        return("Zero")
# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(n):
    result = ""
    for i in range(1,n+1):
        for j in range(1, i + 1):
            result += "*"
        result += "\n"
    return result.strip()


# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ""
    current_num = 1
    while current_num <= limit:
        if current_num % 3 == 0:
            result += "Multiple of 3" + "\n"
        else:
            result += str(current_num) + "\n"
        
        current_num += 1

    return result.strip()

    

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    current = start
    while current <= end:
        if current % 2 == 0:
            total += current
        current += 1

    return total
