"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When letters are inputted rather than numbers.

2. When will a ZeroDivisionError occur?
When you try to divide by 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
No, as long as a numerator and denominator are present within the calculation a zerodivisionerror
will be present if zero is entered for the denominator.

The code has been altered to take into account the zerodiviionerror and this is why
when zero is inputted as the denominator the python interpreter does not crash
but outputs a print statement for the divison by 0 error.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
