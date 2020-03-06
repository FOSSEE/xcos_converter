import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import Element
from xml.etree.ElementTree import Element , SubElement,Comment
from xml.etree.ElementTree import ElementTree
import conf
#/home/eric/IITB/xcos_converter/
tree = ET.parse('example.xml')
root = tree.getroot()
iter = root.getiterator()
ch=root.getchildren()

for i, path in enumerate(conf.path):
    xpath = './/' + path['tag'] 
    #if path.get('attr', None) is not None:
        #path.get('attrvalue', None) is not None
    if 'attr' in path:
        xpath += '[@' + path['attr']
        if 'attrvalue' in path:
            xpath += '=\'' + path['attrvalue'] + '\''
        xpath += ']'    
    
    #print(xpath)
    nodes = root.findall(xpath)
    rl = conf.rule[i]
    for node in nodes:
        if rl['op'] == conf.DOUBLE_TO_INTEGER :
            node.tag = rl['tag']

        if rl['op'] == conf.DELETE_ATTRIB:
            del node.attrib[rl['attr']]

tree.write('new.xml')

# Author - Eric Paul