# question1
chairs = 15
nails = 4
total_nails = chairs * nails
message1 = "I need to buy {} nails".format(total_nails)

print("You need to buy {} nails".format(total_nails))

# question2
# my_name = Penelope   Error: name 'Penelope' is not defined
my_name = "Penelope"
my_age = 29
message2 = "My name is {} and I am {} years old".format(my_name, my_age)

print(message2)

# question3
one_box_eggs = 6
each_omelette_eggs = 4
num_omelette = 9
use_box_of_eggs = each_omelette_eggs * num_omelette // one_box_eggs
# /获得浮点数结果，//获得整数商，math.ceil()进位到下一个整数

message3 = "You can make {} omelettes with {} boxes of eggs".format(num_omelette, use_box_of_eggs)
print(message3)
