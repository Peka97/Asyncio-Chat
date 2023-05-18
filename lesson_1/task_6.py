import locale

with open('test_file.txt', 'w') as f:
	def_coding = locale.getpreferredencoding()
	print(def_coding)
	f.write('сетевое программирование сокет декоратор')

with open('test_file.txt', 'r', encoding='utf-8') as f:
	print(f.read())  # При открытии выдаёт ошибку, т.к. кодировка системы cp1251
	# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
