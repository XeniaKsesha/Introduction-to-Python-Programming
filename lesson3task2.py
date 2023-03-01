eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

language = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
word = input('Введите слово: ').upper()

if language == 1:
	print('Вы заработали', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
elif language == 0:
	print('Вы заработали', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
    print('Вы ввели что-то не то, попробуйте ещё раз')