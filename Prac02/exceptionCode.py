try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# 1. When will a ValueError occur?
# When numerator and denominator are not both postive/negative
# 2. When will a ZeroDivisionError occur?
# If either or both the numerator or denominator are zero
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Loop the question until both values != 0
