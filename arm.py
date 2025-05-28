def is_armstrong(n):
    digits = str(n)
    return sum(int(d) ** len(digits) for d in digits) == n

num = int(input("Enter a number: "))
print("Armstrong number" if is_armstrong(num) else "Not an Armstrong number")
