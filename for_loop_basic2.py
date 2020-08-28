# def biggie_size(listy):
#     for i in range(0, len(listy)):
#       if listy[i] % 2 == 0:
#         listy[i] = "big"
#     return listy
#
# biggie_size([-1,3,5,-5,4])

# def count_positives(listy2):
#     count_positives = 0
#     for item in listy2:
#         if item > 0:
#             count_positives += 1
#     listy2[len(listy2) - 1] = count_positives
#     print (listy2)
#
# count_positives([1, -1, 2, 4, 6, 1])

# def sum_total(listy3):
#     sum_total = 0
#     for item in listy3:
#         sum_total = sum_total + item
#     return(sum_total)
# sum_total([1, -1, 2, 4, 6, 1])
#
# def average(listy4):
#     sum_total = 0
#     for item in listy4:
#         sum_total = sum_total + item
#     average = sum_total/(len(listy4))
#     return(average)
# average([1, -1, 2, 4, 6, 1])

# def length_function(list5):
#     list_length = 0
#     if len(list5) == 0:
#         list_length = False
#     else:
#         list_length = len(list5)
#     return(list_length)
#
# length_function([])

# def minimum_list(list6):
#     if len(list6) == 0:
#         return False
#     else:
#         min_num = list6[0]
#         for x in list6:
#             if x < min_num:
#                 min_num = x
#         return min_num
#
# minimum_list([])

# def maximum_list(list6):
#     if len(list6) == 0:
#         print ("False")
#     else:
#         max_num = list6[0]
#         for x in list6:
#             if x > max_num:
#                 max_num = x
#         print(max_num)
#
# maximum_list([1,2,5,-1])

def ultimate_analysis(list7):
    sum_total = 0
    minimum_value = list7[0]
    maximum_value = list7[0]
    for x in list7:
        if x < minimum_value:
            minimum_value = x
        if x > maximum_value:
            maximum_value = x
        sum_total = sum_total + x
    average = sum_total/(len(list7))
    total_analyis = {
    'sumTotal': sum_total,
    'average': average,
    'minimum': minimum_value,
    'maximum': maximum_value,
    'length': len(list7)
    }
    print(total_analyis)

ultimate_analysis([1,5,2,-3])
