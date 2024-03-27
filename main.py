import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import xml.dom.minidom

df = pd.read_excel("transformed_data.xlsx", dtype=str)
# Create the root element
realty_feed = ET.Element('realty-feed')
realty_feed.set('xmlns', 'http://webmaster.yandex.ru/schemas/feed/realty/2010-06')

# Add generation-date element
generation_date = ET.SubElement(realty_feed, 'generation-date')
generation_date.text = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')

for index, row in df.iterrows():
    offer = ET.SubElement(realty_feed, 'offer')
    offer.set('internal-id', row['id'])
    offer_type = ET.SubElement(offer, 'type')
    offer_type.text = row['type']
    property_type = ET.SubElement(offer, 'property-type')
    property_type.text = row['property-type']
    category = ET.SubElement(offer, 'category')
    category.text = row['category']
    creation_date = ET.SubElement(offer, 'creation-date')
    creation_date.text = row['creation-date']
    location = ET.SubElement(offer, 'location')
    country = ET.SubElement(location, 'country')
    country.text = row['country']
    locality_name = ET.SubElement(location, 'locality-name')
    locality_name.text = row['locality-name']
    address = ET.SubElement(location, 'address')
    address.text = row['address']
    deal_status = ET.SubElement(offer, 'deal-status')
    deal_status.text = row['deal-status']
    price = ET.SubElement(offer, 'price')
    value = ET.SubElement(price, 'value')
    value.text = row['price_value']
    currency = ET.SubElement(price, 'currency')
    currency.text = row['price_currency']
    sales_agent = ET.SubElement(offer, 'sales-agent')
    phone = ET.SubElement(sales_agent, 'phone')
    phone.text = row['phone']
    organization = ET.SubElement(sales_agent, 'organization')
    organization.text = row['organization']
    url = ET.SubElement(sales_agent, 'url')
    url.text = row['url']
    category = ET.SubElement(sales_agent, 'category')
    category.text = row['category']
    rooms = ET.SubElement(offer, 'rooms')
    rooms.text = row['rooms']
    new_flat = ET.SubElement(offer, 'new-flat')
    new_flat.text = row['new-flat']
    floor = ET.SubElement(offer, 'floor')
    floor.text = row['floor']
    floors_total = ET.SubElement(offer, 'floors-total')
    floors_total.text = row['floors-total']
    building_name = ET.SubElement(offer, 'building-name')
    building_name.text = row['building-name']
    yandex_building_id = ET.SubElement(offer, 'yandex-building-id')
    yandex_building_id.text = row['yandex-building-id']
    yandex_house_id = ET.SubElement(offer, 'yandex-house-id')
    yandex_house_id.text = row['yandex-house-id']
    building_state = ET.SubElement(offer, 'building-state') 
    building_state.text = row['building-state']
    ready_quarter = ET.SubElement(offer, 'ready-quarter')
    ready_quarter.text = row['ready-quarter']
    built_year = ET.SubElement(offer, 'built-year')
    built_year.text = row['built-year']
    image = ET.SubElement(offer, 'image')
    image.set('tag', 'plan')
    image.text = row['image']
    area = ET.SubElement(offer, 'area')
    area_value = ET.SubElement(area, 'value')
    area_value.text = row['area_value']
    area_unit = ET.SubElement(area, 'unit')
    area_unit.text = row['area_unit']
    living_space = ET.SubElement(offer, 'living-space')
    living_space_value = ET.SubElement(living_space, 'value')
    living_space_value.text = row['living-space_value']
    living_space_unit = ET.SubElement(living_space, 'unit')
    living_space_unit.text = row['living-space_unit']

tree = ET.ElementTree(realty_feed)
xml_str = ET.tostring(realty_feed, encoding='utf-8', method='xml')
xml_dom = xml.dom.minidom.parseString(xml_str)
pretty_xml_str = xml_dom.toprettyxml(indent="  ", encoding='utf-8')
with open("realty_feed.xml", "wb") as f:
    f.write(pretty_xml_str)

