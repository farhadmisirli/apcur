from app import app, db
import requests

from app.models import Currency
import xml.etree.ElementTree as ET
from datetime import date

today = date.today()
date = today.strftime("%Y-%m-%d")

response = requests.get("https://www.cbar.az/currencies/"+today.strftime("%d.%m.%Y")+".xml")

# mytree = ET.parse('currencies.xml')
mytree = ET.fromstring(response.content)


for x in mytree[1]:
    code = x.attrib.get('Code')
    value = x.find('Value').text
    name = x.find('Name').text

    curr = Currency(code, value, date)
    db.session.add(curr)
    db.session.commit()