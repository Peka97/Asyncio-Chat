import re
import csv


def get_value(text: str, col_name) -> str:
	"""
	Функция получения значения поля из текста.

	:param text: Текст, из которого необходимо достать значение.
	:param col_name: Название колонки, которое нужно будет убрать из текста.
	:return: Значение текста.
	"""

	return text.lstrip(f'{col_name}: ').rstrip('\n')


def check_re(text: str, col_names) -> str | None:
	"""
	Функция проверки на соответствие переданного текста(text) регулярным выражениям(col_names).

	:param text: Текст для проверки.
	:param col_names: Названия столбцов для регулярных выражений.
	:return: Совпавший по регулярному выражению текст, иначе None.
	"""

	for idx, col_name in enumerate(col_names):
		if re.compile(rf'^{col_name}: ').match(text):
			return idx, get_value(text, col_name)
	return None


def get_data(*args: str) -> list[list]:
	"""
	Функция для получения значений 'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы' из файла.

	:param args: Пути до файлов.
	:return: Список столбцов и их значения.
	"""

	main_data = [
		['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
		[],
		[],
		[],
		[]
	]

	for file in args:
		with open(file, 'r', encoding='cp1251') as f:
			for line in f:
				data = check_re(line, main_data[0])
				if data:
					idx, text = data
					main_data[idx + 1].append(text)

	return main_data


def write_to_csv(path: str) -> None:
	"""
	Функция, записывающая результат поиска и форматирования данных из info-файлов.

	:param path: Путь до результирующего файла.
	:return: None
	"""

	data = get_data('src/info_1.txt', 'src/info_2.txt', 'src/info_3.txt')
	with open(path, 'w', encoding='utf-8') as csv_file:
		f_n_writer = csv.writer(csv_file)

		for row in data:
			f_n_writer.writerow(row)


if __name__ == '__main__':
	write_to_csv('src/result_task_1.csv')
