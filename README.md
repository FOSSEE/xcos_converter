# Xcos-Converter

The aim of this project is to provide a software which converts a Scilab 5.5.2 file to Scilab 6.0.2 file. The code is written in python and the package used is Element tree.

## Getting Started

There are two main files used in the project, parser.py & conf.py. Inorder to run the project run the parser.py. The other files present are **the input xcos files for the project**

### Requirement

The technologies required for this project are :

	* Ubuntu 16 & up
	* Python 3.6

Python element tree doesnt need to be installed as it is already present in the python package, it only needs to be imported.

## Running the Project

As mentioned before the two main files for this project are parser.py and conf.py .
Before you run the program make sure the desired input file is given to the code.
 
```
tree = ET.parse('CMSCOPE.xcos')
```
In place of 'CMSCOPE.xcos' you can give your desired file.

The name of the output file produced by the code can also be changed.

```
tree.write('new.xcos', encoding="UTF-8", xml_declaration=True)
```
In place of 'new.xcos' enter your desired name.

Now run parser.py in the terminal as follows :

```
python parser.py
```
Note : Make sure the inputs given to parser are in the same folder. You can check the output by opening the file 'new.xcos' or the name given by you.


## Note

All the latest code have been pushed to the **Python branch in the same repo** , please refer that.
