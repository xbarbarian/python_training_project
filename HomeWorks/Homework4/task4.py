# Home work Lesson 4 Task 4

first_list = [4, 5, 3, 7, 3, 7, 8, 10, 9, 9]
new_list = [el for el in first_list if first_list.count(el) < 2]
print('Изначальный список -', first_list )
print('Преобразованный список -', new_list)
