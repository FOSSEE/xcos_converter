import xml.etree.ElementTree as ET
from xml.dom import minidom

import conf
#/home/eric/IITB/xcos_converter/
tree = ET.parse('example.xml')
data = minidom.parse('example.xml')
root = tree.getroot()
iter = root.getiterator()


for child in root:
    for a in conf.rules:
        if child.tag in conf.rules:
            child.tag== conf.rules[child.tag]

    #accessing grandchild nodes
    for gchild in child:
        if gchild.tag == 'rank':
            print(gchild.text)

#change node based on name       
    if child.tag == 'Xml':
        child.tag ='USA'

#changing  nodes based on attributes
    for elem in iter:
        if elem.keys():
            for name,value in elem.items():
                if value == 'Chile':
                    elem.tag='S.A'
                elif value == 'Singapore':
                    elem.tag='Asia'
                #print(value)


tree.write('new.xml')