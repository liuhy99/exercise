# Question 1
for number in range(100):
    output = 'o' * number
    print(output)
# print(list(range(100)))
# Explain what this program does:
# out put the letter 'o' in number from 0 to 99 times


# Question 2
# What is wrong?
# it does not return the calculated result and by default when return is not specified it return None
# How do you fix it?
def calculate_vat(amount):
    cal = int(amount * 1.2)
    return cal

total = calculate_vat(100)
print(total)
