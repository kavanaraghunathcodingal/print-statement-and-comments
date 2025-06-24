num = int(input("Enter a positive integer: "))
if num == 0:
    print("Binary: 0")
else:
    binary = ""
    while num > 0:
        r = num % 2
        binary = str(r) + binary
        num //= 2
    print("Binary:", binary)
