num = int(input("Enter a number: "))
n = len(str(num))
total = sum([int(d)**n for d in str(num)])

print("Armstrong number" if total == num else "Not an Armstrong number")
