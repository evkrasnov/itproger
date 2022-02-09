# print("Hello, Python! ", 9 + 1, sep="", end="!!!")

# for i in range(7):
#     print(i)

# word = "Какое> небо голубое!"
# print(word)
# list_znk = ['>', '!', '/n']
#
# for i in list_znk:
#     word = word.replace(i, "")
# print(word)
#
# word1 = word.split(" ")
# for i in word1:
#     print(i)
#
# word1 = word.split(" ")
# print(word1)
#
# new_text = ' '.join(word1)
# print(new_text)
#
# r = open("text.txt")
# print(r.read().split())
# r.close()

# with as - не нужно отдельно закрывать файл
try:
    with open("text.txt", encoding='utf-8') as file:
        print(file.read())
except ModuleNotFoundError:
    print('Файл не найден!')

passport = {'Фамилия': 'Иванов', 'Имя': 'Юрий', 'Отчество': 'Петрович', 'Пол': 'мужской'}


for key, values in passport.items():
    print(key, "-", values)
