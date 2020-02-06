import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('/home/eric/IITB/xcos_converter/example.xml')
data = minidom.parse('/home/eric/IITB/xcos_converter/example.xml')
root = tree.getroot()
iter = root.getiterator()


''' for elem in iter:

    if elem.keys():
        for name,value in elem.items():
            if value == 'Liechtenstein':
                value = 'Test3'
                print(value) '''
            



for child in root:
    if child.tag == 'USA':
        child.tag ='Xml'
    for elem in iter:
        if elem.keys():
            for name,value in elem.items():
                if value == 'Singapore':
                    value = 'Test3'
                print(value)


tree.write('/home/eric/IITB/xcos_converter/new.xml')