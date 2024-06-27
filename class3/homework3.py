# question1
ask = input("If it is raining? y/n: ")
if ask == "y":
    print("Take an umbrella")
if ask == "n":
    print("You don't need an umbrella")

# # question2
my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money >= boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

# question3
year = int(input("Which year do you want to choose? from 1800 to 1950: "))

if year>=1800 and year<1810:
    print("Nineteenth Century, Noughties")
elif year>=1810 and year<1820:
    print("Nineteenth Century, Tens")
elif year>=1820 and year<1830:
    print("Nineteenth Century, Twenties")
elif year>=1830 and year<1840:
    print("Nineteenth Century, Thirties")
elif year>=1840 and year<1850:
    print("Nineteenth Century, Forties")
elif year>=1850 and year<1860:
    print("Nineteenth Century, Fifties")
elif year>=1860 and year<1870:
    print("Nineteenth Century, Sixties")
elif year>=1870 and year<1880:
    print("Nineteenth Century, Seventies")
elif year>=1880 and year<1890:
    print("Nineteenth Century, Eighties")
elif year>=1890 and year<1900:
    print("Nineteenth Century, Nineties")
elif year>=1900 and year<1910:
    print("Twenty Century, Noughties")
elif year>=1910 and year<1920:
    print("Twenty Century, Tens")
elif year>=1920 and year<1930:
    print("Twenty Century, Twenties")
elif year>=1930 and year<1940:
    print("Twenty Century, Thirties")
elif year>=1940 and year<1950:
    print("Twenty Century, Forties")
else:
    print("It isn't in stock")
# def categorize_book(year):
#     century = (year - 1) // 100 + 1
#     century_str = ''
#
#     if century == 19:
#         century_str = 'Nineteenth Century'
#     elif century == 20:
#         century_str = 'Twentieth Century'
#
#     decade = (year % 100) // 10 * 10
#     decade_str = ''
#
#     if decade == 0:
#         decade_str = 'Noughties'
#     elif decade == 10:
#         decade_str = 'Tens'
#     elif decade == 20:
#         decade_str = 'Twenties'
#     elif decade == 30:
#         decade_str = 'Thirties'
#     elif decade == 40:
#         decade_str = 'Forties'
#     elif decade == 50:
#         decade_str = 'Fifties'
#     elif decade == 60:
#         decade_str = 'Sixties'
#     elif decade == 70:
#         decade_str = 'Seventies'
#     elif decade == 80:
#         decade_str = 'Eighties'
#     elif decade == 90:
#         decade_str = 'Nineties'
#
#     # Return the formatted string
#     return f"{century_str}, {decade_str}"
#
# print(categorize_book(year))
