"""
Description: Module 05 demonstration: Functions
Author: Anthony Gomes
Date: October 24, 2024
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet() -> None:
    """
    Prints a greeting message to the console.
    When called, this function prints the message "Hello, World!" to the console.

    Args:
        None

    Returns:
        None
    """
    print("Hello, World!")

#Call the function by its name


def greet_name(name: str) -> None:
    """
    Prints a greeting which includes
    the value of the name arguement.

    Args:
        name(str): The name of the person to greet.

    Returns:
        None aka: no value is returned
    """
    print(f"Hello, {name}!")

greet_name("Bob")
greet_name("Annie")
greet_name("Chris")


def greet_name_age(name: str, age: int) -> None:
    """
    Prints a greeting which includes
    the value of the name arguement.

    Args:
        name(str): The name of the person to greet.
        age (int): The age of the person to greet.
    Returns:
        None aka: no value is returned
    """
    print(f"Hello, {name}, you are {age} years old!")

greet_name_age("Annie", 20)
greet_name_age("Bob", 43)


# Function - ARGS AND RETURN
def math_operation(operand1: int, operand2: int, operation: str = "+")-> float:
    """
    Returns the result of the specified operation based
    on the two operands.

    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operand3 (str): The operation to perform, default = "+"
    Returns:
        Result (float): result of the specified operation on two operands.
    Raises:
        ValueError: "Invalid operation." When operation is not + or -.
    """

    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")
    
    return result

try:
    print(math_operation(5,5,))
except ValueError as e:
    print(e)

try:
    print(math_operation(5,5,"*"))
except ValueError as e:
    print(e)

try:
    result = math_operation(1,5,"+")
    print(result)
except ValueError as e:
    print("ERROR:", e)

print(math_operation.__doc__)

print(print.__doc__)
print(input.__doc__)





# New Thing
def display_person_info(name: str, age: int, city: str) -> None:
    """Prints a person's information to the console.

    Given a name, age, and city as arguments, this function prints a message to the console
    describing the person's information.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.
        city (str): The city where the person lives.

    Returns:
        None
    """
    print(f"{name} is {age} years old and lives in {city}.")

display_person_info(name="Alice", city="New York", age=30)




# New Thing
def change_string(input_string: str) -> None:
    """Modifies an input string by appending additional text.

    Args:
        input_string (str): The input string to be modified.

    Returns:
        None
    """
    input_string += " modified inside function"

original_string = "Original string"
change_string(original_string)
print(original_string)  # Output: "Original string"



# New Thing
def my_function() -> None:
    """Prints a local variable to the console.

    This function creates a local variable called 'local_variable' 
    and assigns it the value "I am a local variable". It then prints 
    the value of 'local_variable' to the console.

    Args:
        None

    Returns:
        None
    """
    local_variable = "I am a local variable"
    print(local_variable)

my_function()
# print(local_variable)  # This line would cause an error since local_variable is not defined outside the function



# New Thing
global_variable = "I am a global variable"

def my_function() -> None:
    """Prints a global variable to the console, and modifies it within 
    the function.

    This function prints the value of the global variable 
    'global_variable' to the console. It then modifies the value 
    of 'global_variable' to "I have been modified" using the 
    'global' keyword.

    Args:
        None

    Returns:
        None
    """

    # To modify the global variable within the function
    global global_variable
    print(global_variable)
    global_variable = "I have been modified"
    print(global_variable)

my_function()
print(global_variable)


# New Thing
demo_var = 10  # This is a global variable

def my_function() -> None:
    """Prints a local variable with the same name as a global variable.

    This function creates a local variable called 'demo_var' and 
    assigns it the value 5. It then prints the value of 'demo_var' to the console.

    Args:
        None

    Returns:
        None
    """
    demo_var = 5  # This is a local variable with the same name as the global variable
    print(f"Local demo_var: {demo_var}")

my_function()
print(f"Global demo_var: {demo_var}")

# Output:
# Local demo_var: 5
# Global demo_var: 10