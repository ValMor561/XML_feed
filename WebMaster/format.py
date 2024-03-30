import pandas as pd
from datetime import datetime

def get_category(room):
    if room == '1' or room == '2' or room == '3':
        return str(int(room) + 2)
    else:
        return 6 

df = pd.read_excel("flats.xlsx", dtype=str)
df['id'] = df['ID']
df['rooms'] = df['Число комнат']
df['area_value'] = df['Площадь']
df['name'] = df['rooms'].astype(str) + '-я квартира, ' + df['area_value'].astype(str) + ' м²'
df['url'] = df['id'].apply(lambda x: f"https://ligo.group/flats/{x}/")
df['category'] = df['rooms'].apply(lambda x: get_category(x))
df['price'] = df['Цена']
df['currency'] = 'RUR'
df['image'] = df['Картинка для анонса']
df['conversion'] = 1.0
df['type'] = 'продажа'
df['set-ids'] = df['ID_PROJECT_MACROCRM'].apply(lambda x: f"s{x}")
df['floor'] = df['Этаж']
df['built-year'] = df['Дата ввода'].str.split(' кв. ', expand=True)[1]
df['address'] = df['Полное название ЖК'].str.extract(r'\((.+?)\)')
df['view'] = ''
df.loc[df['Вид'] == 'flat', 'view'] = df['Вид']
df.loc[df['Вид'] != 'flat', 'view'] = pd.NA

df = df.dropna(subset=['view', 'image'])
df.drop(columns=['Картинка для анонса', 'ID', 'Дата сдачи', 'Площадь', 'ID_PROJECT_MACROCRM', 'Полное название ЖК', 'Цена', 'Число комнат', 'Дата ввода', 'Этаж', 'Вид', 'view'], inplace=True)

df.to_excel('transformed_flats.xlsx', index=False)

print('Данные сохранены в transformed_flats.xlsx')

def get_image(row):
    first_image = row['Картинка для анонса']
    other_images = row['Галерея']
    urls = other_images.split("https://ligo.group/upload/iblock")
    urls = urls[1:]
    urls = ["https://ligo.group/upload/iblock" + url for url in urls]
    return [first_image] + urls[:9]

jk = pd.read_excel("jk.xlsx", dtype=str)
jk = jk.dropna(subset=['Картинка для анонса', 'Галерея'])
jk['id'] = jk['ID']
jk['set'] = jk['ComplexId MacroCRM'].apply(lambda x: f"s{x}")
jk['name'] = jk['Название']
jk['vendor'] = "Группа компаний «ЛИГО»"
jk['url'] = jk['Символьный код'].apply(lambda x: f"https://ligo.group/dwellings/{x}/")
jk['categoryId'] = 7
jk['price'] = jk['Временное поле цены']
jk['currency'] = 'RUR'
jk['conversion'] = 1.0
jk['type'] = 'продажа'
jk['set-ids'] = jk['ComplexId MacroCRM'].apply(lambda x: f"s1, s{x}")
jk['addres'] = jk['Адрес'].str.split(':', expand=True)[1]
jk['count'] = jk['ComplexId MacroCRM'].apply(lambda x: df['set-ids'].value_counts().get(f"s{x}"))
jk[['lat', 'long']] = jk['Карта'].str.split(',', expand=True)
jk['description'] = jk['Описание для анонса']
jk['image'] = jk.apply(get_image, axis=1)

jk = jk.dropna(subset=['count'])
jk.drop(columns=['Название', 'ID', 'Символьный код', 'Временное поле цены', 'ComplexId MacroCRM', 'Адрес', 'Карта', 'Описание для анонса', 'Картинка для анонса', 'Галерея'], inplace=True)

jk.to_excel('transformed_jk.xlsx', index=False)

print('Данные сохранены в transformed_jk.xlsx')