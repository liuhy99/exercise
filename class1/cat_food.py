# my code
cats = 10
cans = 20

print("If you want to feed 10 cats, you need " + str(cans) + "cans")
total_cans = cans * 7
print("If you want to feed 10 cats for 7 days, you need " + str(total_cans) + "cans")

# teacher's answer
# setting the variables
num_of_cats = 10
cans_per_cat = 2
days = 7
# calculate total cans
total_cat_cans = num_of_cats * cans_per_cat * days
# result
message = str(num_of_cats) + " cats eat " + str(total_cat_cans) + " cans in " + str(days) + " days"
print(message)

# rewrite use formatting
output = "{} cats eat {} food cans in {} days".format(num_of_cats, total_cat_cans, days)
print(output)

