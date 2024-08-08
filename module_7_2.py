def custom_write(file_name, strings):
    counter = 0
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        counter += 1
        position = file.tell()
        file.write(f'{i}\n')
        strings_positions.update({(counter, position): i})
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
