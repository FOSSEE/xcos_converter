import xml.etree.ElementTree as ET

xmlTree = ET.parse('/home/eric/Documents/example.xml')
xmlRootTag = {elem.tag for elem in xmlTree.iter()}


#xmlTree = ET.parse('/home/fossee/Documents/example.xml')
#xmlRootTag  = list({elem.tag for elem in xmlTree.iter()})

#for xmlChild in xmlRootTag:
    #if xmlChild :
       # print(xmlChild)

for xmlChild in xmlRootTag:
    if xmlChild == 'to':
        xmlChild = 'food'
        #print(xmlChild)
    #else:
        #print(xmlChild)
xmlTree.write('/home/eric/Documents/new.xml')