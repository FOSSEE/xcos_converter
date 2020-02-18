import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import Element
from xml.etree.ElementTree import Element, SubElement
from xml.etree.ElementTree import ElementTree
import conf
#/home/eric/IITB/xcos_converter/
tree = ET.parse('example.xml')
root = tree.getroot()
iter = root.getiterator()
ch=root.getchildren()

ls =['exprs',"nmode"]

for child in root:

    #change node based on name
    '''for q in child:
        if q.tag in conf.rules:
            print(q.tag)
            q.tag = conf.rules[q.tag]'''

    #changing gchild nodes based on child attrib
    for c in child:
        for r in c:
            for n,v in r.items():
                if n in conf.at:
                    for a in conf.a:
                        for b in conf.b:
                            r.set(a,b)

    #changing  nodes based on attributes
    '''for elem in iter:
        if elem.keys():
            for name,value in elem.items():
                if value in conf.r1:
                    elem.tag=conf.r1[value]'''
    


        

tree.write('new.xml')