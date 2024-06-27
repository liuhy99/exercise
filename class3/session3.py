# for number in range(9):
#     print('~' * number)

# exercise 3.1
# price_of_burger = input("Input the price of a burger: ")
# check = float(price_of_burger) <= 10.00
#
# print("Burger is within budget: {}".format(check))

# exercise 3.2
# price_of_burger = input("Input the price of a burger: ")
# vegetarian_option = input("do you have vegetarian option?: ")
# check = float(price_of_burger) <= 10.00
# check_option = vegetarian_option == "y" or vegetarian_option == "yes"
#
# # print("Burger is within budget: {}".format(check))
# print("Restaurant meets criteria: {}".format(check and check_option))

# exercise 3.3
# price_of_burger = input("Input the price of a burger: ")
# vegetarian_option = input("do you have vegetarian option?: ")
# check = float(price_of_burger) <= 10.00
# check_option = vegetarian_option == "y" or vegetarian_option == "yes"
#
# if check and check_option:
#     print("this restaurant is a great choice!")
# if not check and check_option:
#     print("probably not a good idea")

# # exercise 3.4
# meal_price = float(input("How much did the meal cost? "))
# discount_choice = input('Do you have a discount? y/n ')
# discount_applicable = discount_choice == 'y'
#
# if discount_applicable and meal_price >= 20.00:
#     meal_price = meal_price * 0.9
#     print("Discount applied")
# else:
#     print("No discount for you")
#
# print(f'Total cost: {meal_price}')

# exercise 3.5
# temperature = float(input("What is the  temp of the oven?"))
# if temperature > 200:
#     print("The oven is too hot")
# elif temperature < 150:
#     print("The oven is too cold")
# elif temperature == 180:
#     print("The oven is at the perfect temperature")
# else:
#     print("The temperature is close enough")

# exercise 3.6
import random
user_choice = input("coin flip, what's your choice?: ")

def flip_coin():
    random_choice = random.randint(1, 2)
    if random_choice == 1:
        side = "heads"
    else:
        side = "tails"
    return side

result = flip_coin()
print(result)

if user_choice == result:
    print("You won!")
else:
    print("You lose!")