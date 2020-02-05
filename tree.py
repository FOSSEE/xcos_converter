import xml.etree.ElementTree as ET
tree = ET.parse('/home/eric/Documents/example.xml')
root = tree.getroot()
for rank in root.iter('rank'):
    new_rank=int(rank.text) + 2
    rank.text = str(new_rank)
    rank.set('updated','yes')
tree.find('.//year').text = '1/1/2011'

tree.write('/home/eric/Documents/new.xml')