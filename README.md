The aim of this project is to provide a software which converts a Scilab 5.5.2 file to Scilab 6.0.2 file. The code is written in python and the package used is Element tree. Python Element tree is a lxml package and it is a XML.The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.

XPath (XML Path Language) is a query language for selecting nodes from an XML document. XPath uses "path like" syntax to identify and navigate nodes in an XML document.The XPath language is based on a tree representation of the XML document, and provides the ability to navigate around the tree, selecting nodes by a variety of criteria.

Xcos is a Scilab toolbox for modeling and simulation of dynamic (continuous and discrete) systems. Although the main purpose is to simulate dynamic systems.

The relationship between Xcos and Xml is that Xcos is written in the same format as XML with Xcos specific tags. So, we can parse Xcos files as XML files.

The files used in this project are:

1. Parser.py:
The parser file uses conf.py to get the xpath and the rule.The first part of the code deals with xpath. Xpaths are needed to find the exact nodes we have to work with , it guarantees that no other nodes which might have similar tag names are affected. 
Inorder to build the xpath , it refers to the variable path in the conf file. Once the xpath is built it goes through the rule variable in the conf file to find out which operation has to be applied to the node found using xpath.


2. Conf.py

In this file we have globally defined all variables. All the operations that are to be performed are mentioned at the beginning of this file. 
	This file contains two lists i.e. path and rule. 
  
Path :
  Path has nodes like tag, attribute, subtag, sub attributes that are to be changed. It deals with Xpath in the parser.py   	file. This nodes are declared using pattern ‘KEY_PATH_*’.
	Initially, path list is declared empty. Later on nodes get appended to this list according to the requirement of Xpath 			written in the parser.py file.

Rule :
	Rule has a list of nodes with changed values. This nodes are declared using pattern ‘KEY_RULE_*’. 
	At first, this list is empty. When Xpath in the parser.py file gets the desired node, the operation related to it is 				performed. And the list gets appended with changed nodes. The operations are declared using the pattern ‘KEY_RULE_OP’.

