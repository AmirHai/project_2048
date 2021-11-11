# этот класс мне нужен чтобы разобраться во всех ошибках проги
# с помощью него я смотрю на все ошибки и проблемы с базой данных
# отсюда строки кода не брать во внимание и не трогать. они мне нужны для проверки


recordwriting = open(f'../allCSVFiles/records_qwe.csv', 'w', encoding='utf8')
recordwriting.write('dger')
recordwriting.write('hybgfsgdghk')
allrec = open(f'../allCSVFiles/records_qwe.csv', encoding='utf8').readlines()
recordwriting.close()