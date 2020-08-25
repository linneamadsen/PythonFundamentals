# Countdown
def countdown(number):
    elements = []
    for x in range(number, -1, -1):
        elements.append(x)
    return(elements)
countdown(5)

#Print and return

def print_and_return(a):
    print(a[0])
    return a[1]
print_and_return([1,2])

#First plus length

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum
first_plus_length([1,2,3])

#Values Greater than Second
# def values_greater_than_second(list):
#     impt = list[1]
#     total_greater = 0
#     new_list = []
#     for i in list:
#         new_list.append(list[i])
#         if list[i] > impt:
#             total_greater = total_greater + 1
#     print(total_greater)
#     if len(new_list) < 2:
#         print(False)
#     else:
#         print(new_list)
# values_greater_than_second([3,7,5])

#This Length That Value
def this_length_that_value(size, value):
    list = []
    for x in range (0, size):
         list.append(value)
    print(list)
this_length_that_value(4,7)
