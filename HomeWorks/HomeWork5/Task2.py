# # Home Work Lesson 5 Task 2
# # 2. Создать текстовый файл (не программно),
# # сохранить в нем несколько строк, выполнить подсчет количества строк,
# # количества слов в каждой строке.


with open('test_file.txt') as f_read:
    lines = 0
    words = 0

    for line in f_read:
        words_list = line.split()
        lines = lines + 1
        words = words + len(words_list)
print(f'Lines:{lines}')
print(f'Words:{words}')


