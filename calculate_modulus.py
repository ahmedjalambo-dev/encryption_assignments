# Name: Ahmed Marwan Omer Jalambo
# ID: 204911002


def calculate_modulus():
    try:
        # Receive two numbers from the user
        num1 = float(input("Enter the first number (dividend): "))
        num2 = float(input("Enter the second number (divisor): "))

        # Calculate the modulus
        result = num1 % num2

        # Display the result
        print(f"The modulus of {num1} % {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    calculate_modulus()
