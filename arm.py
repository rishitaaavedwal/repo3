num = int(input("Enter a number: "))
print("Armstrong number" if sum(int(d)**len(str(num)) for d in str(num)) == num else "Not an Armstrong number")
class ArmstrongChecker:
    def __init__(self, num):
        self.num = num
    def is_armstrong(self):
        n = len(str(self.num))
        return self.num == sum(int(d)**n for d in str(self.num))
num = int(input("Enter a number: "))
checker = ArmstrongChecker(num)
print("Armstrong number" if checker.is_armstrong() else "Not an Armstrong number")
num = int(input("Enter a number: "))
digits = list(map(int, str(num)))
n = len(digits)
total = sum(map(lambda x: x ** n, digits))
print("Armstrong number" if total == num else "Not an Armstrong number")