import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import Element
from xml.etree.ElementTree import Element , SubElement
from xml.etree.ElementTree import ElementTree
import conf
#/home/eric/IITB/xcos_converter/
tree = ET.parse('example.xml')
root = tree.getroot()
iter = root.getiterator()
ch=root.getchildren()

for i, path in enumerate(conf.path):
    xpath = './/' + path['tag'] + '[@' + path['attr'] + '=\'' + path['attrvalue'] + '\']'
    #print(xpath)
    nodes = root.findall(xpath)
    #nd = root.find(xpath)
    for node in nodes:
        if node.tag == path['tag']:
            node.tag="ScilabInteger"
        for n in node:
            for a,b in n.items():
                if a == 'realPart': 
                    b=str(int(float(b)))
                    n.attrib[a] = b
                    n.attrib['value'] = n.attrib[a]
                    del n.attrib[a]

tree.write('new.xml')