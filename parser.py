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


for child in root:

    #change node based on attrib
    for q in child:
        for n,v in q.items():
            if q.attrib[n] in conf.attr:
                if q.tag in conf.rules:
                    q.tag = conf.rules[q.tag]

    #setting new in attrib
    for c in child:
        for r in c:
            for n,v in r.items():
                if n in conf.at:
                    for a in conf.a:
                        for b in conf.b:
                            r.set(a,b)

    #changing  attributes names & values
    for c in child:
        for r in c:
            for n,v in r.items():
                if n in  conf.lst:
                    v = str(int(float(v)))
                    r.attrib[n] = v
                    for t in conf.t:
                        r.attrib[t] = r.attrib[n]
                        del r.attrib[n]
                        print(r.attrib)

    # adding new element
                            
    

#remove nodes based on attributes
for child in ch:
    for gchild in child:
        for n,v in gchild.items():
            if gchild.attrib[n] in conf.ls:
                child.remove(gchild)
        

tree.write('new.xml')