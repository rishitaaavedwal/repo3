num = int(input("Enter a number: "))
original = num
n = len(str(num))
result = 0

while num > 0:
    digit = num % 10
    result += digit ** n
    num //= 10

print("Armstrong number" if result == original else "Not an Armstrong number")
