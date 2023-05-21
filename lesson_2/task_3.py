import yaml


def load_to_yaml(data_to_yaml: dict) -> None:
	"""
	Функция загрузки данных в YAML.

	:param data_to_yaml: Данные для загрузки.
	:return: None
	"""

	with open('src/result_task_3.yaml', 'w', encoding='utf-8') as y_f:
		yaml.dump(data_to_yaml, y_f, default_flow_style=False, allow_unicode=True)


def dump_from_yaml(path: str) -> dict:
	"""
	Функция загрузки данных из YAML по указанному пути(path).

	:param path: Путь до файла.
	:return: Данные из файла.
	"""

	with open(path, 'r', encoding='utf-8') as y_f:
		return yaml.load(y_f, yaml.FullLoader)


if __name__ == '__main__':
	data = {
		'♗': [1, 2, 3],
		'♖': 10,
		'♕': {
			'key':
				{'key': 'value'}
		},

	}
	load_to_yaml(data)  # Загружаем данные в YAML
	data_from_yaml = dump_from_yaml('src/result_task_3.yaml')  # Грузим данные из YAML
	print(data == data_from_yaml)  # Проверка на соответствие данных
