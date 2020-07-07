# Write a function is_even that will return true if the passed-in number is even.

def simple_even(n):
    """Evaluates a number to determine the truth of it being even.

    Args:
        n (a number): An int or float that represents some number.

    Yields:
        True / False (bool) True if the number is even, else False.
    """
    try:
        validation = n % 2 == 0

    except TypeError:
        validation = int(n) % 2 == 0

    finally:
        return validation


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if simple_even(num) == True:
    print("Even!")
else:
    print("Odd")
