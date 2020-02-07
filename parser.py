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
    if child.tag == 'Xml':
        child.tag ='USA'

    for elem in iter:
        if elem.keys():
            for name,value in elem.items():
                if value == 'Chile':
                    elem.tag='SA'
                elif value == 'Singapore':
                    elem.tag='Asia'
                #print(value)


tree.write('/home/eric/IITB/xcos_converter/new.xml')