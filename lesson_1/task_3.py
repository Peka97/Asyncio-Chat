def str_to_bytes(arr: tuple | list) -> list:
	result = []

	for word in arr:  # Таким методом у меня ошибок нет
		try:
			word = word.encode()
		except UnicodeEncodeError:
			result.append(word)
	return result


if __name__ == '__main__':
	words = (
		'attribute',
		'класс',
		'функция',
		'type'
	)
	print(str_to_bytes(words))
