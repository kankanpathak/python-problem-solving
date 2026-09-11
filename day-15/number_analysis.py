def analyze_number(n):
    positive_negative_zero = ""
    even_odd = "No even / odd"

    if n > 0:
        positive_negative_zero = "Positive"
        if n % 2 == 0:
            even_odd = "Even"
        else:
            even_odd = "Odd"

    elif n < 0:
            positive_negative_zero = "Negative"
            if n % 2 == 0:
                even_odd = "Even"
            else:
                even_odd = "Odd"
    else:
        positive_negative_zero = "Zero"

    digits = 0

    if n < 0:
        n = n * - 1

    if n == 0:
        digits = 1
    else:
        while n > 0:
            num = n % 10
            n = n // 10
            digits += 1

    return f"{positive_negative_zero}\n{even_odd}\nDigits: {digits}"


print(analyze_number(246))
print(analyze_number(-57))
print(analyze_number(0))
