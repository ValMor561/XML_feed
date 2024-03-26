import pandas as pd
from datetime import datetime

def from_roman(str):
    roman_dict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
    return roman_dict[str]

def get_yandex_building_id(building_name):
    building_name_lower = building_name.lower()
    matched_row = index_df[index_df['name_jk'].str.lower() == building_name_lower]
    if not matched_row.empty:
        return matched_row.iloc[0]['yandex-building-id']
    else:
        return None

def get_house_building_id(house):
    house_name_lower = str(house).lower()
    matched_row = index_df[index_df['house'].str.lower() == house_name_lower]
    if not matched_row.empty:
        return matched_row.iloc[0]['yandex-house-id']
    else:
        return None


df = pd.read_excel("1.xlsx")
index_df = pd.read_excel('index.xlsx', dtype=str)
df['image'] = df['Картинка для анонса']
df['type'] = 'продажа'
df['property-type'] = 'жилая'
df['category'] = 'квартира'
df['creation-date'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')
df['id'] = df['ID']
df['area_value'] = df['Площадь']
df['area_unit'] = 'кв. м'
df['living-space_value'] = df['Площадь']
df['living-space_unit'] = 'кв. м'
df['country'] = 'Россия'
df['locality-name'] = 'Южно-Сахалинск'
df['address'] = df['Полное название ЖК'].str.extract(r'\((.+?)\)')
df['deal-status'] = 'первичная продажа'
df['building-name'] = df['Полное название ЖК'].str.extract(r'ЖК «(.+?)»')
df['yandex-building-id'] = df['building-name'].apply(lambda x: get_yandex_building_id(x))
house = lambda x: x.split()[-1].replace(".", "")
df['yandex-house-id'] = df['address'].apply(house).apply(lambda x:  get_house_building_id(x))
df['building-state'] = 'unfinished'
df['price_value'] = df['Цена']
df['price_currency'] = 'RUR'
df['phone'] = '+7979147570727'
df['organization'] = 'Группа компаний "ЛИГО"'
df['url'] = 'https://ligo.group/'
df['category'] = 'developer'
df['rooms'] = df['Число комнат']
df['new-flat'] = 1
df[['ready-quarter', 'built-year']] = df['Дата ввода'].str.split(' кв. ', expand=True)
df['ready-quarter'] = df['ready-quarter'].apply(lambda x: from_roman(x) if pd.notna(x) else pd.NA)
df['floors-total'] = ''
df['floor'] = df['Этаж']


    
df.drop(columns=['Картинка для анонса', 'ID', 'Дата сдачи', 'Площадь', 'Полное название ЖК', 'Цена', 'Число комнат', 'Дата ввода', 'Этаж'], inplace=True)
df.to_excel('transformed_data.xlsx', index=False)