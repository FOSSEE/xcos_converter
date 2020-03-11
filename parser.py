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
    #print(i, xpath, rl , nodes)
    for node in nodes:
        
        #print(node.tag)
        if rl['op'] == conf.CHANGE_ATTRIB:
            pass 

        elif rl['op'] == conf.DOUBLE_TO_INTEGER :
            node.tag = rl['tag']
            for n ,v in rl['attribute'].items():
                node.set(n,v)
            if 'attr1' in path:
                x = './/'+ path['subtag']
                n = node.find(x)
                n.attrib[rl['attr']] =  str(int(float(n.attrib[path['attr1']])))
                del n.attrib[path['attr1']]

                
        elif rl['op'] == conf.DELETE_ATTRIB:
            if rl['attr'] in node.attrib:
                del node.attrib[rl['attr']]


        elif rl['op'] == conf.MAIN_BLOCK:
            pass


        elif rl['op'] == conf.ADD_SUB_SUBTAG:
            pass


        elif rl['op'] == conf.DELETE_SUBTAG:
            pass


        elif rl['op'] == conf.DOUBLE_TO_INTEGER_AND_SWAP:
            pass


        elif rl['op'] == conf.DELETE_SUB_ATTRIB:
            pass


        elif rl['op'] == conf.DELETE_SUBSUB_ATTRIB:
            pass

        
            
                
#print(conf.rule)
comment = Comment('Xcos - 2.0 - scilab-6.0.2 - 20190911')
root.insert(0,comment)
tree.write('new.xml', encoding='UTF-8', xml_declaration = True)

# Author - Eric Paul