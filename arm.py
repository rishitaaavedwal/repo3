num = int(input("Enter a number: "))
digits = list(map(int, str(num)))
n = len(digits)
total = sum(map(lambda x: x ** n, digits))

print("Armstrong number" if total == num else "Not an Armstrong number")
