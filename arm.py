def armstrong_recursive(num, n):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** n + armstrong_recursive(num // 10, n)

num = int(input("Enter a number: "))
n = len(str(num))
print("Armstrong number" if armstrong_recursive(num, n) == num else "Not an Armstrong number")
