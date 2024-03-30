import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import xml.dom.minidom
# Создаем корневой элемент
yml_catalog = ET.Element('yml_catalog', {'date': datetime.now().strftime("%Y-%m-%d %H-%M")})

# Создаем элемент <shop> и его дочерние элементы
shop = ET.SubElement(yml_catalog, 'shop')
name = ET.SubElement(shop, 'name')
name.text = 'Купить квартиру'
company = ET.SubElement(shop, 'company')
company.text = 'Группа компаний «ЛИГО»'
url = ET.SubElement(shop, 'url')
url.text = 'https://ligo.group/'
email = ET.SubElement(shop, 'email')
email.text = 'realty@sample.s3.yandex.net'

# Добавляем валюты
currencies = ET.SubElement(shop, 'currencies')
currency = ET.SubElement(currencies, 'currency', {'id': 'RUR', 'rate': '1'})

# Добавляем категории
categories = ET.SubElement(shop, 'categories')
category1 = ET.SubElement(categories, 'category', {'id': '1'})
category1.text = 'Квартира'
category2 = ET.SubElement(categories, 'category', {'id': '2', 'parentId': '1'})
category2.text = 'Студия'
category3 = ET.SubElement(categories, 'category', {'id': '3', 'parentId': '1'})
category3.text = '1-комнатная'
category4 = ET.SubElement(categories, 'category', {'id': '4', 'parentId': '1'})
category4.text = '2-комнатная'
category5 = ET.SubElement(categories, 'category', {'id': '5', 'parentId': '1'})
category5.text = '3-комнатная'
category6 = ET.SubElement(categories, 'category', {'id': '6', 'parentId': '1'})
category6.text = '4-к и более'
category7 = ET.SubElement(categories, 'category', {'id': '7'})
category7.text = 'Жилой комплекс'

jk = pd.read_excel("transformed_jk.xlsx", dtype=str)

# Добавляем наборы
sets = ET.SubElement(shop, 'sets')
set1 = ET.SubElement(sets, 'set', {'id': 's1'})
set1_name = ET.SubElement(set1, 'name')
set1_name.text = 'Квартиры от застройщика в Южно-Сахалинске — группа компаний «ЛИГО»'
set1_url = ET.SubElement(set1, 'url')
set1_url.text = 'https://ligo.group/projects/'
# Добавьте остальные наборы здесь
for index, row in jk.iterrows():
    set = ET.SubElement(sets, 'set', {'id': row['set']})
    set_name = ET.SubElement(set, 'name')
    set_name.text = row['name']
    set_url = ET.SubElement(set, 'url')
    set_url.text = row['url']



offers = ET.SubElement(shop, 'offers')

for index, row in jk.iterrows():

    offer = ET.SubElement(offers, "offer")
    offer.set("id", row['id'])

    name = ET.SubElement(offer, "name")
    name.text = row['name']

    vendor = ET.SubElement(offer, "vendor")
    vendor.text = row['vendor']

    url = ET.SubElement(offer, "url")
    url.text = row['url']

    categoryId = ET.SubElement(offer, "categoryId")
    categoryId.text = row['categoryId']

    price = ET.SubElement(offer, "price")
    price.set("from", "true")
    price.text = row['price']

    currencyId = ET.SubElement(offer, "currencyId")
    currencyId.text = row['currency']

    param1 = ET.SubElement(offer, "param")
    param1.set("name", "Конверсия")
    param1.text = row['conversion']

    param2 = ET.SubElement(offer, "param")
    param2.set("name", "Тип предложения")
    param2.text = row['type']

    set_ids = ET.SubElement(offer, "set-ids")
    set_ids.text = row['set-ids']

    param3 = ET.SubElement(offer, "param")
    param3.set("name", "Число объявлений")
    param3.text = row['count']

    param4 = ET.SubElement(offer, "param")
    param4.set("name", "Адрес")
    param4.text = row['addres']

    param5 = ET.SubElement(offer, "param")
    param5.set("name", "Широта")
    param5.text = row['lat']

    param6 = ET.SubElement(offer, "param")
    param6.set("name", "Долгота")
    param6.text = row['long']

    description = ET.SubElement(offer, "description")
    description.text = row['description']

    # Добавление картинок
    pictures = eval(row['image'])

    for picture_url in pictures:
        picture = ET.SubElement(offer, "picture")
        picture.text = picture_url

df = pd.read_excel("transformed_flats.xlsx", dtype=str)
for index, row in df.iterrows():
    offer = ET.SubElement(offers, "offer")
    offer.set("id", row['id'])

    # Добавляем дочерние элементы в <offer>
    name = ET.SubElement(offer, "name")
    name.text = row['name']

    url = ET.SubElement(offer, "url")
    url.text = row['url']

    categoryId = ET.SubElement(offer, "categoryId")
    categoryId.text = row['category']

    price = ET.SubElement(offer, "price")
    price.text = row['price']

    currencyId = ET.SubElement(offer, "currencyId")
    currencyId.text = row['currency']

    picture = ET.SubElement(offer, "picture")
    picture.text = row['image']

    param1 = ET.SubElement(offer, "param", name="Конверсия")
    param1.text = row['conversion']

    param2 = ET.SubElement(offer, "param", name="Тип предложения")
    param2.text = row['type']

    set_ids = ET.SubElement(offer, "set-ids")
    set_ids.text = row['set-ids']

    param3 = ET.SubElement(offer, "param", name="Этаж")
    param3.text = row['floor']

    param4 = ET.SubElement(offer, "param", name="Площадь")
    param4.text = row['area_value']

    param5 = ET.SubElement(offer, "param", name="Год постройки")
    param5.text = row['built-year']

    param6 = ET.SubElement(offer, "param", name="Число комнат")
    param6.text = row['rooms']

    param7 = ET.SubElement(offer, "param", name="Адрес")
    param7.text = row['address']

tree = ET.ElementTree(yml_catalog)
xml_str = ET.tostring(yml_catalog, encoding='utf-8', method='xml')
xml_dom = xml.dom.minidom.parseString(xml_str)
pretty_xml_str = xml_dom.toprettyxml(indent="  ", encoding='utf-8')
with open("realty_feed.yml", "wb") as f:
    f.write(pretty_xml_str)
print("Данные записаны в файл realty_feed.yml")