import xml.etree.ElementTree as ET
import conf
#/home/eric/IITB/xcos_converter/
tree = ET.parse('example.xml')
root = tree.getroot()
iter = root.getiterator()
ch=root.getchildren()

ls =["Singapore","Panama"]

for child in root:
    
    #remove parent tag by searching attrib
    '''for elem in iter:
        for child in list(elem):
            if child.tag in conf.ls:
                elem.remove(child)
                '''
    #change node based on name
    '''for a in conf.rules:
        if child.tag in conf.rules:
            child.tag = conf.rules[child.tag]'''

    #changing gchild nodes based on child attrib
    for n,v in child.items():
        if v == 'Singapore':
            for r in child:
                if r.tag=='rank':
                    r.tag="test2"
            

    #changing  nodes based on attributes
    '''for elem in iter:
        if elem.keys():
            for name,value in elem.items():
                if value in conf.r1:
                    elem.tag=conf.r1[value]'''
    
    
'''for child in ch:
    for n,v in child.items():
        if child.attrib[n] in ls:
            print(child.tag)
            root.remove(child)'''
     

tree.write('new.xml')