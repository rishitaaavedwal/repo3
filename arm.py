num = int(input("Enter a number: "))
print("Armstrong number" if sum(int(d)**len(str(num)) for d in str(num)) == num else "Not an Armstrong number")
