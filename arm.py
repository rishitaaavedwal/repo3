num = int(input("Enter a number: "))
digits = str(num)
n = len(digits)
total = 0

for d in digits:
    total += int(d) ** n

print("Armstrong number" if total == num else "Not an Armstrong number")
