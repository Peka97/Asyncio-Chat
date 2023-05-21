words = ('разработка', 'сокет', 'декоратор')

for word in words:
	print(type(word), word)

words = (
	u'%u0440%u0430%u0437%u0440%u0430%u0431%u043E%u0442%u043A%u0430',
	u'%u0441%u043E%u043A%u0435%u0442',
	u'%u0434%u0435%u043A%u043E%u0440%u0430%u0442%u043E%u0440'
)

for word in words:
	print(type(word), word)
