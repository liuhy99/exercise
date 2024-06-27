# # question1
# shopping_list =[
#     "oranges",
#     "cat food",
#     "sponge cake",
#     "long-grain rice",
#     "cheese board",
# ]
# # the index of list is from 0, so if you want to see the first thing, you need to use the index of 0 like this
# print(shopping_list[0])

# # question2
# chocolates = {
#     "white": 1.50,
#     "milk": 1.20,
#     "dark": 1.80,
#     "vegan": 2.00,
# }
# input = input("input an item: ")
# if input == "white":
#     print(chocolates['white'])
# elif input == "milk":
#     print(chocolates['milk'])
# elif input == "dark":
#     print(chocolates['dark'])
# elif input == "vegan":
#     print(chocolates['vegan'])

# question3
import random
numbers = [1,2,3,4,5,6,7]
random_numbers = [random.randint(1,10) for i in range(7)]
print(numbers)
print(random_numbers)
# compare
matches = 0
for item in numbers:
    if item in random_numbers:
        matches += 1

if matches == 3:
    print("£20 for three matching numbers")
elif matches == 4:
    print("£40 for four matching numbers")
elif matches == 5:
    print("£100 for five matching numbers")
elif matches == 6:
    print("£10000 for six matching numbers")
elif matches == 7:
    print("£1000000 for seven matching numbers")
else:
    print("sorry, no prize")