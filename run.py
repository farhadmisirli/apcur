from app import app
import requests

# import routes
from app import routes

import requests
import xml.etree.ElementTree as ET

response = requests.get("https://www.cbar.az/currencies/19.03.2021.xml")
root = ET.fromstring(response.content)


for child in root.iter('*'):
    print(child.tag)


if __name__ == "__main__":
	app.run(debug=True)

