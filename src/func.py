# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_even(n):
    if int(n) % 2 == 0:
        print("Even!")
        return True
    else:
        print("Odd")
        return False

is_even(num)