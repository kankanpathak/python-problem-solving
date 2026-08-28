n = int(input("Enter a number: "))

og_digit = n
reverse = 0

while n > 0:
    reverse = n % 10 + reverse * 10
    n = n // 10

if reverse == og_digit:
    print("Palindrome")
else:
    print("Not a Palindrome")
