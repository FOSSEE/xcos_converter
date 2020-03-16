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
       
                
        elif rl['op'] == conf.DELETE_ATTRIB :                       #deleting attrib ordering
            if rl['attr'] in node.attrib:
                del node.attrib[rl['attr']]


        elif rl['op'] == conf.MAIN_BLOCK:
            a = SubElement(node,rl['tag'],rl['attr'])
            a.tail = '\n      '
            if rl['attr1'] not in node.attrib:          #add attrib dependsOnU if not present
                node.set(rl['attr1'],rl['value'])
            for n,v in rl['attribute'].items():         #add attrib dependsOnT
                node.set(n,v)

        elif rl['op'] == conf.ADD_SUB_SUBTAG :
            x = './/'+ path['subtag']
            n = node.find(x)                # finding mxgeometry
            xp = './/'+ path['subtag'] +'['+ rl['subsubtag']+']'
            np= node.find(xp)               # finding mx point tag in mxgeometry
            if np is None:
                a = SubElement(n,rl['subsubtag'],rl['attr'])
                a.tail = "\n        "
                b = SubElement(n,rl['subsubtag1'],rl['attr1'])
                b.tail = "\n        "       


        elif rl['op'] == conf.DELETE_SUBTAG:            #removing mxgeometry tag
            if 'subtag' in path:
                x = './/'+ path['subtag']
                n = node.find(x)
                node.remove(n)
            if len(node.getchildren()) == 0:
                node.text=None


        elif rl['op'] == conf.DOUBLE_TO_INTEGER_AND_SWAP:
            if int(node.attrib['height']) > 0:
                node.tag = rl['tag']            #change tag
                node.attrib['height'],node.attrib['width'] = node.attrib['width'],node.attrib['height']     #exchange height & width
                x = './/'+ path['subtag'] + '[@' + path['subattr'] +']'         #xpath for data
                m = node.findall(x)
                for n in m:
                    n.attrib[rl['attr']] =  str(int(float(n.attrib[path['subattr']])))          #change to value
                    del n.attrib[path['subattr']]
                    n.attrib['column'],n.attrib['line'] = n.attrib['line'],n.attrib['column']   #exchange line & column

                for n ,v in rl['attribute'].items():
                    node.set(n,v)


        elif rl['op'] == conf.DELETE_SUB_ATTRIB:                #delete subattrib 'y' from mxGeometry
            x = './/'+ path['subtag']
            n = node.find(x)
            if rl['attr'] in n.attrib:
                del n.attrib[rl['attr']]


        elif rl['op'] == conf.DELETE_SUBSUB_ATTRIB:             #delete attrib scilabclass from array
            x ='.//' + path['subsubtag']
            n = node.find(x)
            del n.attrib[rl['attr']]
            
        elif rl['op'] == conf.ADD_ATTRIB:
            for k, v in rl['attribute'].items():                #add attrib initialport
                node.set(k,v)
            if rl['attr'] not in node.attrib:                   # if attrib 'datalines' is not present add
                node.set(rl['attr'],rl['value'])
        

root.text= None
root.text = "\n  "
comment = Comment("Xcos - 2.0 - scilab-6.0.2 - 20190911")
comment.tail = "\n      "  
root.insert(0,comment)
tree.write('new.xml', encoding='UTF-8', xml_declaration=True)

# Author - Eric Paul