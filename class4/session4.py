# list
# exercise4.1
# clothes = [
#     "shorts",
#     "shoes",
#     "t-shirts",
# ]
# if clothes[0] == "shorts":
#     clothes[0] = "warm coat"
# else:
#     print("the first item is not shorts")
#
# print(clothes)

# list functions
# sorted(): specific for list
# reversed(): also for others   use:reverse=True
# exercise 4.2
# scores = [3,6,70,89,199,200,43,55,10,7]
# print("number of scores: ", len(scores))
# print("highest score", max(scores))
# print("lowest of scores: ", min(scores))
# print("descending of scores: ", sorted(scores, reverse=True))
# print("increasing of scores: ", sorted(scores))

# exercise4.3
# shopping_list = ["bread","oil","shampoo","water"]
# if "bread" in shopping_list:
#     shopping_list.append("butter")
#
# print(shopping_list)

# combine for loops and lists
# exercise 4.4
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
# for item in costs:
#     # total_cost = total_cost + item
#     total_cost += item
# print(total_cost)
#
# total = sum(costs)
# print(total)

# dictionaries
# place = {
#     'name': "the Anchor",
#     "post_code": "E14 6HY",
#     "street_number": "54",
#     "location":{
#         "longitude": 127,
#         "latitude":63,
#     }
# }
#
# print(place['name'],
#       place['post_code'],
#       place['street_number'],
#       place['location']['longitude'],
#       place['location']['latitude'])
# # 在一条print里面换行输出
# print(place['name']+'\n'+ place['post_code']+'\n'+ place['street_number'])
#       # place['location']['longitude']+"\n"+
#       # place['location']['latitude'])
#
# place["city"] = "London"
# print(place)
#
# # another way to print longitude and latitude
# loc = place['location']
# print(loc["longitude"])

# exercise 4.6
# fruits = [
#     {"name": "apple", "colour": "red", "price": 0.12},
#     {"name": "banana", "colour": "yellow", "price": 0.2},
#     {"name": "pear", "colour": "green", "price": 0.19}
# ]
#
# for item in fruits:
#     print(item['name'])
#     print(item['colour'])
#     print(item['price'])

# exercise 4.7
import random
firstname_list = ["elina","jully","mia"]
lastname_list = ["white","black"]

chosen_firstname = random.choice(firstname_list)
chosen_lastname = random.choice(lastname_list)
print(f"a random name: {chosen_firstname} {chosen_lastname}")



