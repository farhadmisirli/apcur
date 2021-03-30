from app import app, db
from app.models import Currency
from datetime import date
import requests
import xml.etree.ElementTree as ET

today = date.today()
date = today.strftime("%Y-%m-%d")

response = requests.get("https://www.cbar.az/currencies/"+today.strftime("%d.%m.%Y")+".xml")
mytree = ET.fromstring(response.content)

for x in mytree[1]:
    code = x.attrib.get('Code')
    value = x.find('Value').text
    name = x.find('Name').text

    curr = Currency(code, value, date)
    db.session.add(curr)
    db.session.commit()