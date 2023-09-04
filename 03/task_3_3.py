k = 'lizard'

eng_alpha = 'qwertyuiopasdfghjklzxcvbnm'
rus_alpha = 'йцукенгшщзхъфывапролджэячсмитьбюё'

eng = {1:'AEIOULNSTR',
       2:'DG',
       3:'BCMP',
       4:'FHVWY',
       5:'K',
       8:'JX',
       10:'QZ'}

rus = {1:'АВЕИНОРСТ',
       2:'ДКЛМПУ',
       3:'БГЁЬЯ',
       4:'ЙЫ',
       5:'ЖЗХЦЧ',
       8:'ШЭЮ',
       10:'ФЩЪ'}

points_table = [eng, rus]
points_sum = 0

if k[0].lower() in eng_alpha:
    lang = points_table.index(eng) #ID 0 for the English dictionary
else:
    lang = points_table.index(rus) #ID 1 for the Russian dictionary

for letter in k:
    for key, value in points_table[lang].items():
        if letter.upper() in value:
            points_sum += key

print(points_sum)