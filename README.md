# python-learning-session-using-hacker-rank

I am building new things day by day using python this is my part of journey with the python learning, I am using a most popular page@ hackerrank.com to improve my self...thanks to @AlgonexITSolutions

## Code

```python
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
```

## Topics Covered

- **Palindrome Check**: Validates if a string is a palindrome
- **String Reversal**: Reverses strings using Python slicing
- **Integer vs Float Division**: Demonstrates the difference between `//` and `/` operators
- **User Input**: Takes input from users and processes it

## How to Run

```bash
python hackerrankproblems.py
```
