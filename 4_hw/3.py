def file_mutations(text: str, name: str):
    file = open(name, 'a+', encoding='utf-8')

    # единственная реализация, которую нашел чтобы не пропускать строку в новом файле
    if file.tell() == 0:
        file.write(f'{text}')
    else:
        file.write(f'\n{text}')
    file.close()

    print("Информация из четных строк файла:\n")

    with open(name, 'r') as file:
        for index, string in enumerate(file.readlines()):
            if index % 2 == 1:
                continue
            print(f'{string}\n')
            
file_mutations('ya ustala', 'text1.txt')