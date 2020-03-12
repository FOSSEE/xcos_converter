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

        if rl['op'] == conf.DOUBLE_TO_INTEGER :
            node.tag = rl['tag']
            for n ,v in rl['attribute'].items():
                node.set(n,v)
            if 'subattr' in path:
                x = './/'+ path['subtag'] + '[@' + path['subattr'] +']'
                m = node.findall(x)
                for n in m:
                    n.attrib[rl['attr']] =  str(int(float(n.attrib[path['subattr']])))
                    del n.attrib[path['subattr']]
 
                
                
        ecdlif rl['op'] == conf.DELETE_ATTRIB:
            if rl['attr'] in node.attrib:
                del node.attrib[rl['attr']]


        elif rl['op'] == conf.MAIN_BLOCK:
            pass


        elif rl['op'] == conf.ADD_SUB_SUBTAG:
            pass


        elif rl['op'] == conf.DELETE_SUBTAG:
            if 'subtag' in path:
                x = './/'+ path['subtag']
                n = node.find(x)
                node.remove(n)
            if len(node.getchildren()) == 0:
                node.text=None


        elif rl['op'] == conf.DOUBLE_TO_INTEGER_AND_SWAP:
            if int(node.attrib['height']) > 1:
                node.tag = rl['tag']            #change tag
                node.attrib['height'],node.attrib['width'] = node.attrib['width'],node.attrib['height']     #exchange height & width
                x = './/'+ path['subtag'] + '[@' + path['subattr'] +']'         #xpath for data
                m = node.findall(x)
                for n in m:
                    n.attrib[rl['attr']] =  str(int(float(n.attrib[path['subattr']])))          #change to value
                    del n.attrib[path['subattr']]
                    n.attrib['column'],n.attrib['line'] = n.attrib['line'],n.attrib['column']   #exchange line & column

        elif rl['op'] == conf.DELETE_SUB_ATTRIB:
            if 'subtag' in path:
                x = './/'+ path['subtag']
                n = node.find(x)
                del n.attrib[rl['attr']]


        elif rl['op'] == conf.DELETE_SUBSUB_ATTRIB:
            x ='.//' + path['subsubtag']
            n = node.find(x)
            del n.attrib[rl['attr']]
            

        
            
                
#print(conf.rule)
comment = Comment('Xcos - 2.0 - scilab-6.0.2 - 20190911')
root.insert(0,comment)
tree.write('new.xml', encoding='UTF-8', xml_declaration = True)

# Author - Eric Paul