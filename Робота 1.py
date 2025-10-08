print("Hello World!")
print()
print('test')

# однорядковий коментар

'''
три одинарні лапки
багаторядковий
коментар
тут можна писати будь яктй текст і він буде проігнорований інтерпетатором
'''

# Ctrl + / -> comment или uncomment

print("Hello World!")
print('qqqqq')
# sdfgsdfgsdfg
print('test')

####
# escape послідовності
# \n -> перенесення на новий рядок
print("Hallo\nworld")
# \t -> табуляція -> 4 пробіли. (буває в консолі 2 або 8 пробіли)
print("Hello\n\tWorld")
# \ -> дзеркалювання, екранування - якщо необхідно службовий символ зробити друкованим
print("He\\llo\\n\\t\"world")
print("\\\\\\\\\\")

#####
print("Hello World!", "Test info", "Demo text", sep=", ", end="-")
print("Hello World!")

# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних : True False
# str -> рядов -масим (набір) символів