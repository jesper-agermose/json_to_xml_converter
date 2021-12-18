from json2xml import json2xml
from json2xml.utils import readfromjson
from configparser import ConfigParser

if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')
    org_dir = config.get('config', 'org') #file.json
    dest_dir = config.get('config', 'dest') #file.xml

    data = readfromjson(org_dir)
    xml = json2xml.Json2xml(data, wrapper="countries", pretty=True, attr_type=True).to_xml()

    with open(dest_dir, 'w') as c:
        c.write(xml)
        print("Wrote xml file to " + dest_dir )