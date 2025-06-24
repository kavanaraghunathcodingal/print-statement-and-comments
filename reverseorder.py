num = input("Enter a number: ")
sign = ''
if num.startswith('-'):
    sign = '-'
    num = num[1:]

# Reverse the string and keep non-digits if you want
rev = num[::-1]

print("Reversed:", sign + rev)
