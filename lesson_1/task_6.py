import locale

def_coding = locale.getpreferredencoding()  # cp1251
print(def_coding)
with open('test_file.txt', 'r', encoding='utf-8') as f:
	print(f.read())  # У меня ошибок нет
