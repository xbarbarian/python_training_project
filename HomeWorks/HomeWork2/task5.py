# Home work lesson 2 task 5
rating_list = [7, 5, 3, 3, 2]

while True:
    try:
        new_rating = int(input('введи целое число \n'))
        # print('это целое число')
        break
    except:
        print('это не целое число, попробуй еще раз')
rating_count = rating_list.count(new_rating)

# print(rating_count)

if not rating_count:
    if new_rating > rating_list[0]:
        rating_list.insert(0, new_rating)
    elif new_rating < rating_list[-1]:
        rating_list.append(new_rating)
else:
    # print('есть одинаковые элементы списка')

#     while i < len(rating_list):
#         # print(i)
#         if new_rating == rating_list[i] and rating_count == 1:
#             new_rating_idx = rating_list[i]
#             rating_list.insert(new_rating_idx, new_rating)
#             print(new_rating_idx)
#             break
#         elif new_rating == rating_list[i]:
#             new_rating_idx = rating_list[i + rating_count]
#
#             rating_list.insert(new_rating_idx, new_rating)
#             break
#         else:
#             i += 1
#
# print(rating_list)

    for id,  in enumerate(rating_list):

