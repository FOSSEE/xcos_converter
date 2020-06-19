import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement, Comment
import conf
import confsb
tree = ET.parse('CMSCOPE.xcos')
root = tree.getroot()
iter = root.getiterator()

for i, path in enumerate(conf.path):

    xpath = './/' + path[conf.KEY_PATH_TAG]                 # making xpath from the variables present in path

    if conf.KEY_PATH_ATTR in path:
        xpath += '[@' + path[conf.KEY_PATH_ATTR]
        if conf.KEY_PATH_ATTRVALUE in path:
            xpath += '=\'' + path[conf.KEY_PATH_ATTRVALUE] + '\''
        xpath += ']'

    # print(xpath)
    nodes = root.findall(xpath)

    rl = conf.rule[i]
    # print(nodes)
    for node in nodes:
        if rl[conf.KEY_RULE_OP] == conf.DOUBLE_TO_INTEGER:
            node.tag = rl[conf.KEY_RULE_TAG]                        # scilabdouble changed to scilabinteger
            for n, v in rl[conf.KEY_RULE_ATTRIBUTE].items():
                node.set(n, v)                                      # set intPrecision32
            if conf.KEY_PATH_SUBATTR in path:
                x = './/' + path[conf.KEY_PATH_SUBTAG] + '[@' + path[conf.KEY_PATH_SUBATTR] + ']'
                m = node.findall(x)
                for n in m:
                    n.attrib[rl[conf.KEY_RULE_ATTR]] = str(int(float(n.attrib[path[conf.KEY_PATH_SUBATTR]])))       # change realpart to value , change double to integer
                    del n.attrib[path[conf.KEY_PATH_SUBATTR]]

        elif rl[conf.KEY_RULE_OP] == conf.DELETE_ATTRIB:                       # deleting attrib of selected node
            if rl[conf.KEY_RULE_ATTR] in node.attrib:
                del node.attrib[rl[conf.KEY_RULE_ATTR]]

        elif rl[conf.KEY_RULE_OP] == conf.MAIN_BLOCK:
            a = SubElement(node, rl[conf.KEY_RULE_TAG], rl[conf.KEY_RULE_ATTR])     # add tags ScilabDouble with attribs state and dstate
            a.tail = '\n      '
            if rl[conf.KEY_RULE_ATTR1] not in node.attrib:          # add attrib dependsOnU if not present
                node.set(rl[conf.KEY_RULE_ATTR1], rl[conf.KEY_RULE_VALUE])
            for n, v in rl[conf.KEY_RULE_ATTRIBUTE].items():         # add attrib dependsOnT
                node.set(n, v)

        elif rl[conf.KEY_RULE_OP] == conf.ADD_SUB_SUBTAG:
            x = './/' + path[conf.KEY_PATH_SUBTAG]
            n = node.find(x)                # finding mxgeometry
            xp = './/' + path[conf.KEY_PATH_SUBTAG] + '[' + rl[conf.KEY_RULE_SUBSUBTAG] + ']'
            np = node.find(xp)               # finding mx point tag in mxgeometry
            if np is None:
                a = SubElement(n, rl[conf.KEY_RULE_SUBSUBTAG], rl[conf.KEY_RULE_ATTR])          #add tag mxPoint
                a.tail = "\n        "
                if conf.KEY_RULE_SUBSUBTAG1 in rl:
                    b = SubElement(n, rl[conf.KEY_RULE_SUBSUBTAG1], rl[conf.KEY_RULE_ATTR1])    
                    b.tail = "\n        "

        elif rl[conf.KEY_RULE_OP] == conf.DELETE_SUBTAG:            # removing mxgeometry tag
            x = './/' + rl[conf.KEY_RULE_SUBTAG]
            n = node.find(x)
            if n is not None:
                node.remove(n)
            if len(node) == 0:
                node.text = None

        elif rl[conf.KEY_RULE_OP] == conf.DOUBLE_TO_INTEGER_AND_SWAP:

            if int(node.attrib['height']) > 0:
                node.attrib['height'], node.attrib['width'] = node.attrib['width'], node.attrib['height']     # exchange height & width
                for n in node:
                    n.attrib['column'], n.attrib['line'] = n.attrib['line'], n.attrib['column']   # exchange line & column

                if conf.KEY_PATH_SUBATTR in path:
                    x = './/' + path[conf.KEY_PATH_SUBTAG] + '[@' + path[conf.KEY_PATH_SUBATTR] + ']'         # xpath for data
                    m = node.findall(x)
                    for n in m:
                        node.tag = rl[conf.KEY_RULE_TAG]            # change tag
                        n.attrib[rl[conf.KEY_RULE_ATTR]] = str(int(float(n.attrib[path[conf.KEY_PATH_SUBATTR]])))          # change to value
                        del n.attrib[path[conf.KEY_PATH_SUBATTR]]

                    for n, v in rl[conf.KEY_RULE_ATTRIBUTE].items():
                        node.set(n, v)

        elif rl[conf.KEY_RULE_OP] == conf.DELETE_SUB_ATTRIB:                # delete subattrib 'x' & 'y' from mxGeometry
            a = './/' + path[conf.KEY_PATH_SUBTAG]
            n = node.find(a)
            if rl[conf.KEY_RULE_ATTR] in n.attrib:
                del n.attrib[rl[conf.KEY_RULE_ATTR]]
            if rl[conf.KEY_RULE_ATTR1] in n.attrib:
                del n.attrib[rl[conf.KEY_RULE_ATTR1]]

        elif rl[conf.KEY_RULE_OP] == conf.DELETE_SUBSUB_ATTRIB:             # delete attrib scilabclass from array
            x = './/' + path[conf.KEY_PATH_SUBSUBTAG]
            n = node.find(x)
            if n is not None:
                del n.attrib[rl[conf.KEY_RULE_ATTR]]

        elif rl[conf.KEY_RULE_OP] == conf.ADD_ATTRIB:
            if conf.KEY_RULE_ATTRIBUTE in rl:
                for k, v in rl[conf.KEY_RULE_ATTRIBUTE].items():                # add new attributes to the given tag
                    node.set(k, v)
            if conf.KEY_RULE_ATTR in rl:
                if rl[conf.KEY_RULE_ATTR] not in node.attrib:                   # if attrib 'datalines' is not present add
                    node.set(rl[conf.KEY_RULE_ATTR], rl[conf.KEY_RULE_VALUE])

        elif rl[conf.KEY_RULE_OP] == conf.DELETE_TAG:
            if conf.KEY_RULE_ATTR in rl:
                xp = node.findall('.//' + rl[conf.KEY_RULE_TAG] + '[@' + rl[conf.KEY_RULE_ATTR] + '=\'' + rl[conf.KEY_RULE_ATTRVALUE] + '\']')
                for n in xp:
                    if xp is not None:
                        node.remove(n)
            else:
                if node is not None:
                    root.remove(node)

        elif rl[conf.KEY_RULE_OP] == conf.REPLACE_ATTRIB:
            del node.attrib[path[conf.KEY_PATH_ATTR]]                       #delete the old attrib
            node.set(rl[conf.KEY_RULE_ATTR], rl[conf.KEY_RULE_VALUE])       # set new attrib

        elif rl[conf.KEY_RULE_OP] == conf.ADD_TAG:
            if conf.KEY_RULE_ATTR in rl:
                xp = node.find('.//' + rl[conf.KEY_RULE_TAG] + '[@' + rl[conf.KEY_RULE_ATTR] + '=\'' + rl[conf.KEY_RULE_ATTRVALUE] + '\']')
            if xp not in node:
                a = SubElement(node, rl[conf.KEY_RULE_TAG], rl[conf.KEY_RULE_ATTRIBUTE])
                a.tail = '\n      '

        elif rl[conf.KEY_RULE_OP] == conf.BLOCK_TYPE_H:

            if conf.KEY_RULE_SUBTAG in rl:
                xp = node.find('.//' + rl[conf.KEY_RULE_SUBTAG])
                if conf.KEY_RULE_SUBATTRVALUE in rl:
                    xp = node.find('.//' + rl[conf.KEY_RULE_SUBTAG] + '[@' + rl[conf.KEY_RULE_SUBATTR] + '=\'' + rl[conf.KEY_RULE_SUBATTRVALUE] + '\']')
                if xp is not None:
                    a = SubElement(xp, rl[conf.KEY_RULE_TAG], rl[conf.KEY_RULE_ATTR])
                    a.tail = '\n      '

            elif conf.KEY_RULE_TAG in rl:
                a = SubElement(node, rl[conf.KEY_RULE_TAG], rl[conf.KEY_RULE_ATTR])
                a.tail = '\n      '


for n, v in conf.root.items():
    root.set(n, v)
root.text = None
root.text = "\n  "
comment = Comment("Xcos - 2.0 - scilab-6.0.2 - 20190911")
comment.tail = "\n      "
root.insert(0, comment)
tree.write('new.xcos', encoding="UTF-8", xml_declaration=True)
