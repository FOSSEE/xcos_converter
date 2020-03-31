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
    xpath = './/' + path[conf.KEY_PATH_TAG] 
    #if path.get('attr', None) is not None:
        #path.get('attrvalue', None) is not None
    if conf.KEY_PATH_ATTR in path:
        xpath += '[@' + path[conf.KEY_PATH_ATTR]
        if conf.KEY_PATH_ATTRVALUE in path:
            xpath += '=\'' + path[conf.KEY_PATH_ATTRVALUE] + '\''
        xpath += ']'    

    #print(xpath)
    nodes = root.findall(xpath)
    rl = conf.rule[i]
    #print(i, rl , nodes)
    for node in nodes:
        
        #print(node.tag) 

        if rl[conf.KEY_RULE_OP] == conf.DOUBLE_TO_INTEGER :
            node.tag = rl[conf.KEY_RULE_TAG]
            for n ,v in rl[conf.KEY_RULE_ATTRIBUTE].items():
                node.set(n,v)
            if 'subattr' in path:
                x = './/'+ path[conf.KEY_PATH_SUBTAG] + '[@' + path[conf.KEY_PATH_SUBATTR] +']'
                m = node.findall(x)
                for n in m:
                    n.attrib[rl[conf.KEY_RULE_ATTR]] =  str(int(float(n.attrib[path[conf.KEY_PATH_SUBATTR]])))
                    del n.attrib[path[conf.KEY_PATH_SUBATTR]]
       
                
        elif rl[conf.KEY_RULE_OP] == conf.DELETE_ATTRIB :                       #deleting attrib ordering
            if rl[conf.KEY_RULE_ATTR] in node.attrib:
                del node.attrib[rl[conf.KEY_RULE_ATTR]]



        elif rl[conf.KEY_RULE_OP] == conf.MAIN_BLOCK:
            a = SubElement(node,rl[conf.KEY_RULE_TAG],rl[conf.KEY_RULE_ATTR])
            a.tail = '\n      '
            if rl[conf.KEY_RULE_ATTR1] not in node.attrib:          #add attrib dependsOnU if not present
                node.set(rl[conf.KEY_RULE_ATTR1],rl[conf.KEY_RULE_VALUE])
            for n,v in rl[conf.KEY_RULE_ATTRIBUTE].items():         #add attrib dependsOnT
                node.set(n,v)


        elif rl[conf.KEY_RULE_OP] == conf.ADD_SUB_SUBTAG :
            x = './/'+ path[conf.KEY_PATH_SUBTAG]
            n = node.find(x)                # finding mxgeometry
            xp = './/'+ path[conf.KEY_PATH_SUBTAG] +'['+ rl[conf.KEY_RULE_SUBSUBTAG]+']'
            np= node.find(xp)               # finding mx point tag in mxgeometry
            if np is None:
                a = SubElement(n,rl[conf.KEY_RULE_SUBSUBTAG],rl[conf.KEY_RULE_ATTR])
                a.tail = "\n        "
                b = SubElement(n,rl[conf.KEY_RULE_SUBSUBTAG1],rl[conf.KEY_RULE_ATTR1])
                b.tail = "\n        "       


        elif rl[conf.KEY_RULE_OP] == conf.DELETE_SUBTAG:            #removing mxgeometry tag
            if 'subtag' in path:
                x = './/'+ path[conf.KEY_PATH_SUBTAG]
                n = node.find(x)
                node.remove(n)
            if len(node.getchildren()) == 0:
                node.text=None


        elif rl[conf.KEY_RULE_OP] == conf.DOUBLE_TO_INTEGER_AND_SWAP:
            if int(node.attrib['height']) > 0:
                node.tag = rl[conf.KEY_RULE_TAG]            #change tag
                node.attrib['height'],node.attrib['width'] = node.attrib['width'],node.attrib['height']     #exchange height & width
                x = './/'+ path[conf.KEY_PATH_SUBTAG] + '[@' + path[conf.KEY_PATH_SUBATTR] +']'         #xpath for data
                m = node.findall(x)
                for n in m:
                    n.attrib[rl[conf.KEY_RULE_ATTR]] =  str(int(float(n.attrib[path[conf.KEY_PATH_SUBATTR]])))          #change to value
                    del n.attrib[path[conf.KEY_PATH_SUBATTR]]
                    n.attrib['column'],n.attrib['line'] = n.attrib['line'],n.attrib['column']   #exchange line & column

                for n ,v in rl[conf.KEY_RULE_ATTRIBUTE].items():
                    node.set(n,v)


        elif rl[conf.KEY_RULE_OP] == conf.DELETE_SUB_ATTRIB:                #delete subattrib 'y' from mxGeometry
            a = './/'+ path[conf.KEY_PATH_SUBTAG]
            n = node.find(a)
            if rl[conf.KEY_RULE_ATTR] in n.attrib :
                del n.attrib[rl[conf.KEY_RULE_ATTR]]
            if rl[conf.KEY_RULE_ATTR1] in n.attrib :
                del n.attrib[rl[conf.KEY_RULE_ATTR1]]


        elif rl[conf.KEY_RULE_OP] == conf.DELETE_SUBSUB_ATTRIB:             #delete attrib scilabclass from array
            x ='.//' + path[conf.KEY_PATH_SUBSUBTAG]
            n = node.find(x)
            del n.attrib[rl[conf.KEY_RULE_ATTR]]


        elif rl[conf.KEY_RULE_OP] == conf.ADD_ATTRIB:
            if conf.KEY_RULE_ATTRIBUTE in rl:
                for k, v in rl[conf.KEY_RULE_ATTRIBUTE].items():                #add attrib initialport
                    node.set(k,v)
            if conf.KEY_RULE_ATTR in rl:
                if rl[conf.KEY_RULE_ATTR] not in node.attrib:                   # if attrib 'datalines' is not present add
                    node.set(rl[conf.KEY_RULE_ATTR],rl[conf.KEY_RULE_VALUE])            


        elif rl[conf.KEY_RULE_OP] == conf.ADD_LINK_ATTRIB:
            for n ,v in rl[conf.KEY_RULE_ATTRIBUTE].items():
                node.set(n,v)


        elif rl[conf.KEY_RULE_OP] == conf.DELETE_TAG:
            root.remove(node)


        elif rl[conf.KEY_RULE_OP] == conf.REPLACE_ATTRIB :
            del node.attrib[path[conf.KEY_PATH_ATTR]]
            node.set(rl[conf.KEY_RULE_ATTR],rl[conf.KEY_RULE_VALUE])

        elif rl[conf.KEY_RULE_OP] == conf.BLOCK_TYPE_C:
            if rl[conf.KEY_RULE_ATTR] not in node.attrib:
                node.set(rl[conf.KEY_RULE_ATTR],rl[conf.KEY_RULE_VALUE])

        elif rl[conf.KEY_RULE_OP] == conf.ADD_TAG:
            #if rl[conf.KEY_PATH_ATTR] in path:
                #if rl[conf.KEY_PATH_ATTRVALUE] in path:
                    #if rl[conf.KEY_RULE_ATTR] not in node.attrib: 
            a = SubElement(node,rl[conf.KEY_RULE_TAG],rl[conf.KEY_RULE_ATTR])
            a.tail = "\n        "
                        

        elif rl[conf.KEY_RULE_OP] == conf.BLOCK_TYPE_H:
            if 'tag' in rl:
                a = SubElement(node,rl[conf.KEY_RULE_TAG],rl[conf.KEY_RULE_ATTR])
                a.tail = "\n        "

for n,v in conf.root.items():
    root.set(n,v)
root.text= None
root.text = "\n  "
comment = Comment("Xcos - 2.0 - scilab-6.0.2 - 20190911")
comment.tail = "\n      "  
root.insert(0,comment)
tree.write('new.xml', encoding='UTF-8', xml_declaration=True)














# Author - Eric Paul