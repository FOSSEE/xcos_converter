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
        for n,v in rl.items():
            if n == 1 :
                node.tag = v['tag']
                print(v['attribute'])

            if n == 3:
                print(v['attr'])
                del node.attrib[v['attr']]
tree.write('new.xml')

# Author - Eric Paul