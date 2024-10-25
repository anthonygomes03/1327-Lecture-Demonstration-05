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
