import xml.etree.ElementTree as ET

tree = ET.parse('/home/eric/IITB/Xcos-Converter/xcos_converter/example.xml')
root = tree.getroot()

for child in root:
    child.tag ='hey'

    print(child.tag,child.attrib)

tree.write('/home/eric/Documents/new.xml')