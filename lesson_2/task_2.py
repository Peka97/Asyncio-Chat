import json
import datetime


def write_order_to_json(item: str, quantity: int, price: int, buyer: str, date: datetime) -> None:
	"""
	Функция записи в файл orders.json данных по полям переданных параметров.

	:param item: Наименование товара.
	:param quantity: Количество товара.
	:param price: Цена товара.
	:param buyer: Имя покупателя.
	:param date: Дата покупки.
	:return: None
	"""

	with open('src/orders.json', 'r', encoding='utf-8') as j_f:
		data = json.load(j_f)
		data['orders'].append(
			{
				'item': item,
				'quantity': quantity,
				'price': price,
				'buyer': buyer,
				'date': str(date)
			}
		)
	with open('src/orders.json', 'w', encoding='utf-8') as j_f:
		json.dump(data, j_f, indent=4)


if __name__ == '__main__':
	write_order_to_json('item_name', 10, 100, 'buyer_name', datetime.date.today())
