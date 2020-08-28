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

def length_function(list5):
    list_length = 0
    if len(list5) == 0:
        list_length = False
    else:
        list_length = len(list5)
    return(list_length)

length_function([])
