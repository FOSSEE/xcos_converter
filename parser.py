import xml.etree.ElementTree as ET

tree = ET.parse('/home/eric/IITB/Xcos-Converter/xcos_converter/example.xml')
root = tree.getroot()

for child in root:
    child.tag ='test1'

    print(child.tag,child.attrib)

tree.write('/home/eric/IITB/Xcos-Converter/xcos_converter/new.xml')