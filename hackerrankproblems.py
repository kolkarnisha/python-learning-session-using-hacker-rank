def is_palindrome(j):
    # Remove spaces and convert to lowercase for a fair comparison
    cleaned = ''.join(j.split()).lower()
    # Check if the cleaned string is the same forwards and backwards
    return cleaned == cleaned[::-1]

# Let's test it out!
print(is_palindrome("radar"))  # This should return True
print(is_palindrome("hello"))  # This should return False
print("")
def reverse_string(text):
    # Remove spaces and convert to lowercase if you want
    cleaned = ''.join(text.split()).lower()
    # Reverse it using slicing
    return cleaned[::-1]

# Take input from user
user_input = input("Enter a string: ")
print(user_input)
reversed_text = reverse_string(user_input)
print("Reversed string:", reversed_text)
print("this was a play with strings its an amazing concept suported by python")
print("""The provided code stub reads two integers,  and , from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  // . 
The second line should contain the result of float division,  / 
""")
if __name__ == '__main__':
    a = int(input("enter your first number: "))
    b = int(input("enter your second number: "))
    print(a//b)
    print(a/b)
print("write a function to return addition, subraction,multiplication,division,floor division of \n two user input numbers")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def nisha():
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    floor_division = num1 // num2
    print(f"addition of two numbers:{addition} \n, subbration of two numbers:{subtraction} \n, multiplication of two numbers:{multiplication} \n, division of two numbers:{division} \n, floor division of two numbers:{floor_division}")

    
nisha()


            
