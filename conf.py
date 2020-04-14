DOUBLE_TO_INTEGER = 1
DELETE_ATTRIB = 2
MAIN_BLOCK = 3
ADD_SUB_SUBTAG = 4
DELETE_SUBTAG = 5
DOUBLE_TO_INTEGER_AND_SWAP = 6
DELETE_SUB_ATTRIB = 7
DELETE_SUBSUB_ATTRIB = 8
ADD_ATTRIB = 9
ADD_LINK_ATTRIB = 10
DELETE_TAG = 11
REPLACE_ATTRIB = 12
BLOCK_TYPE_C = 13
ADD_TAG = 14
ADD_SUBTAG = 15
BLOCK_TYPE_H = 16
KEY_RULE_OP = 'op'
KEY_RULE_TAG = 'tag'
KEY_RULE_ATTRIBUTE = 'attribute'
KEY_RULE_ATTR = 'attr'
KEY_RULE_VALUE = 'value'
KEY_RULE_ATTR1 = 'attr1'
KEY_RULE_ATTRVALUE = 'attrvalue'
KEY_RULE_SUBTAG = 'subtag'
KEY_RULE_SUBATTR = 'subattr'
KEY_RULE_SUBATTRVALUE = 'subattrvalue'
KEY_RULE_SUBSUBTAG = 'subsubtag'
KEY_RULE_SUBSUBTAG1 = 'subsubtag1'
KEY_PATH_TAG = 'tag'
KEY_PATH_ATTR = 'attr'
KEY_PATH_ATTR1 = 'attr1'
KEY_PATH_ATTRVALUE = 'attrvalue'
KEY_PATH_SUBTAG = 'subtag'
KEY_PATH_SUBATTR = 'subattr'
KEY_PATH_SUBSUBTAG = 'subsubtag'


path = []
rule = []

root = {'debugLevel':'0', 'integratorAbsoluteTolerance': '1.0E-6' , 'integratorRelativeTolerance' : '1.0E-6' , 'toleranceOnTime' : '1.0E-10', 'maxIntegrationTimeInterval' : '100001.0' , 'maximumStepSize' : '0.0' , 'realTimeScaling' : '0.0' , 'solver' : '1.0', 'gridEnabled' : '1' }

path.append(
    {
        KEY_PATH_TAG: 'ScilabDouble',
        KEY_PATH_ATTR: 'as',
        KEY_PATH_ATTRVALUE: 'nmode',
        KEY_PATH_SUBTAG:'data',
        KEY_PATH_SUBATTR:'realPart'
    })
rule.append({
    KEY_RULE_OP : DOUBLE_TO_INTEGER,
    KEY_RULE_TAG : 'ScilabInteger',
    KEY_RULE_ATTRIBUTE:{'intPrecision':'sci_int32'},
    KEY_RULE_ATTR:'value'
})



path.append(    
    {
        KEY_PATH_TAG: 'ScilabDouble',
        KEY_RULE_ATTR : 'as',
        KEY_PATH_ATTRVALUE : 'nbZerosCrossing',
        KEY_PATH_SUBTAG : 'data',
        KEY_PATH_SUBATTR : 'realPart'
    })
rule.append({
    KEY_RULE_OP : DOUBLE_TO_INTEGER,
    KEY_RULE_TAG : 'ScilabInteger',
    KEY_RULE_ATTRIBUTE:{'intPrecision':'sci_int32'},
    KEY_RULE_ATTR:'value'
})



path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        
    })
rule.append({
    KEY_RULE_OP : DELETE_ATTRIB,
    KEY_RULE_ATTR : 'ordering'
})

path.append(
    {
        KEY_PATH_TAG : 'BasicBlock',
        
    })
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG : 'ScilabDouble',
    KEY_RULE_ATTR : {'as':'state','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE : {'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        
    })
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG : 'ScilabDouble',
    KEY_RULE_ATTR : {'as':'dState','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE : {'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})



path.append(
    {
        KEY_PATH_TAG :'Product',
        
    })
rule.append({
    KEY_RULE_OP : DELETE_ATTRIB,
    KEY_RULE_ATTR : 'ordering'
})

path.append(
    {
        KEY_PATH_TAG :'Product',
        
    })
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG : 'ScilabDouble',
    KEY_RULE_ATTR : {'as':'state','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE : {'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})

path.append(
    {
        KEY_PATH_TAG :'Product',
        
    })
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG : 'ScilabDouble',
    KEY_RULE_ATTR : {'as':'dState','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE:{'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})


path.append(
    {
        KEY_PATH_TAG :'BigSom',
        
    })
rule.append({
    KEY_RULE_OP : DELETE_ATTRIB,
    KEY_RULE_ATTR : 'ordering',
})

path.append(
    {
        KEY_PATH_TAG :'BigSom',
        
    })
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG : 'ScilabDouble',
    KEY_RULE_ATTR : {'as':'state','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE : {'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})

path.append(
    {
        KEY_PATH_TAG :'BigSom',
        
    })
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR :{'as':'dState','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE:{'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})



path.append(
    {
        KEY_PATH_TAG :'AfficheBlock',
        
    }
)
rule.append({
    KEY_RULE_OP:DELETE_ATTRIB,
    KEY_RULE_ATTR:'ordering',
})
path.append(
    {
        KEY_PATH_TAG :'AfficheBlock',
        
    }
)
rule.append({
    KEY_RULE_OP : MAIN_BLOCK,
    KEY_RULE_TAG :'ScilabDouble',
    KEY_RULE_ATTR : {'as':'state','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE : {'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})

path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        
    }
)
rule.append({
    KEY_RULE_OP:DELETE_ATTRIB,
    KEY_RULE_ATTR:'ordering',
})



path.append(
    {
        KEY_PATH_TAG :'ExplicitLink',
        KEY_PATH_SUBTAG :'mxGeometry',
    }
)
rule.append({
    KEY_RULE_OP : DELETE_SUB_ATTRIB,
    KEY_RULE_ATTR : 'y',
    KEY_RULE_ATTR1 : 'x',
})

path.append(
    {
        KEY_PATH_TAG :'ExplicitLink',
        KEY_PATH_SUBTAG :'mxGeometry',
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_SUB_SUBTAG,
    KEY_RULE_SUBSUBTAG:'mxPoint',
    KEY_RULE_ATTR:{'as':'sourcePoint','x':'0.0','y':'0.0'},
    KEY_RULE_SUBSUBTAG1:'mxPoint',
    KEY_RULE_ATTR1:{'as':'targetPoint','x':'0.0','y':'0.0'}
})


path.append(
    {
        KEY_PATH_TAG :'ExplicitLink',
        KEY_PATH_SUBTAG :'mxGeometry',
        KEY_PATH_SUBSUBTAG :'Array',
    }
)
rule.append({
    KEY_RULE_OP:DELETE_SUBSUB_ATTRIB,
    KEY_RULE_ATTR:'scilabClass',
})

path.append(
    {
        KEY_PATH_TAG :'ExplicitLink',
        
    }
)
rule.append({
    KEY_RULE_OP : ADD_LINK_ATTRIB,
    KEY_RULE_ATTRIBUTE : {'style' : 'ExplicitLink' , 'value' : ''} ,
})

path.append(
    {
        KEY_PATH_TAG :'CommandControlLink',
        
    }
)
rule.append({
    KEY_RULE_OP : ADD_LINK_ATTRIB,
    KEY_RULE_ATTRIBUTE : {'style' : 'CommandControlLink' , 'value' : ''} ,
})


path.append(
    {
        KEY_PATH_TAG :'ExplicitInputPort',
        KEY_PATH_SUBTAG :'mxGeometry' ,
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'mxGeometry',
})


path.append(
    {
        KEY_PATH_TAG :'ExplicitInputPort',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTRIBUTE:{'initialState':'-1.0'},

})


path.append(
    {
        KEY_PATH_TAG :'ExplicitInputPort',
        KEY_PATH_ATTR : 'dataType',
        KEY_PATH_ATTRVALUE : 'REAL_MATRIX',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTR : 'dataColumns',
    KEY_RULE_VALUE: "-2"
})


path.append(
    {
        KEY_PATH_TAG :'ExplicitInputPort',
        KEY_PATH_ATTR : 'dataType',
        KEY_PATH_ATTRVALUE : 'REAL_MATRIX',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTR : 'dataLines',
    KEY_RULE_VALUE: "-1"
})


path.append(
    {
        KEY_PATH_TAG : 'ExplicitInputPort' ,
        KEY_RULE_ATTR : 'visible'

    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB ,
        KEY_RULE_ATTR : 'value' ,
        KEY_RULE_VALUE : ''
    }
)

path.append(
    {
        KEY_PATH_TAG : 'ExplicitInputPort',
        KEY_RULE_ATTR : 'dataType',
        KEY_RULE_ATTRVALUE : 'UNKNOW_TYPE',
    }
)
rule.append({
    KEY_RULE_OP : REPLACE_ATTRIB,
    KEY_RULE_ATTR : 'initialState',
    KEY_RULE_VALUE : '-1.0'
})

path.append(
    {
        KEY_PATH_TAG :'ExplicitOutputPort',
        KEY_PATH_SUBTAG :'mxGeometry' ,
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'mxGeometry',
})

path.append(
    {
        KEY_PATH_TAG :'ExplicitOutputPort',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTRIBUTE:{'initialState':'-1.0'},
})


path.append(
    {
        KEY_PATH_TAG :'ExplicitOutputPort',
        KEY_PATH_ATTR : 'dataType',
        KEY_PATH_ATTRVALUE : 'REAL_MATRIX',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTR : 'dataColumns',
    KEY_RULE_VALUE: "-2"
})


path.append(
    {
        KEY_PATH_TAG :'ExplicitOutputPort',
        KEY_PATH_ATTR : 'dataType',
        KEY_PATH_ATTRVALUE : 'REAL_MATRIX',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTR : 'dataLines',
    KEY_RULE_VALUE: "-1"
})


path.append(
    {
        KEY_PATH_TAG : 'ExplicitOutputPort' ,
        KEY_PATH_ATTR : 'visible'

    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB ,
        KEY_RULE_ATTR : 'value' ,
        KEY_RULE_VALUE : ''
    }
)

path.append(
    {
        KEY_PATH_TAG : 'ExplicitOutputPort',
        KEY_RULE_ATTR : 'dataType',
        KEY_RULE_ATTRVALUE : 'UNKNOW_TYPE',
    }
)
rule.append({
    KEY_RULE_OP : REPLACE_ATTRIB,
    KEY_RULE_ATTR : 'initialState',
    KEY_RULE_VALUE : '-1.0'
})

path.append(
    {
        KEY_PATH_TAG :'ControlPort',
        KEY_PATH_SUBTAG :'mxGeometry' ,
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'mxGeometry',
})

path.append(
    {
        KEY_PATH_TAG :'ControlPort',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTRIBUTE:{'initialState':'-1.0'},
    KEY_RULE_ATTR : 'value',
    KEY_RULE_VALUE : ""
})

path.append(
    {
        KEY_PATH_TAG :'ControlPort',
        
    }
)
rule.append({
    KEY_RULE_OP:DELETE_ATTRIB,
    KEY_RULE_ATTR:'dataType',
})


path.append(
    {
        KEY_PATH_TAG : 'ScilabDouble',
        KEY_PATH_ATTR : 'as',
        KEY_PATH_ATTRVALUE : 'integerParameters',
        KEY_PATH_SUBTAG:'data',
        KEY_PATH_SUBATTR :'realPart'
    })
rule.append({
    KEY_RULE_OP:DOUBLE_TO_INTEGER_AND_SWAP,
    KEY_RULE_TAG:'ScilabInteger',  
    KEY_RULE_ATTRIBUTE:{'intPrecision':'sci_int32'},
    KEY_RULE_ATTR:'value'
})


path.append(
    {
        KEY_PATH_TAG : 'ScilabDouble',
        KEY_PATH_ATTR : 'as',
        KEY_PATH_ATTRVALUE : 'dState',
    })
rule.append({
    KEY_RULE_OP:DOUBLE_TO_INTEGER_AND_SWAP,
})



path.append(
    {
        KEY_PATH_TAG : 'mxPoint',
        KEY_PATH_ATTR : 'as',
        KEY_PATH_ATTRVALUE : 'origin'
    }
)
rule.append(
    {
        KEY_RULE_OP : DELETE_TAG,
        KEY_RULE_TAG : 'mxPoint'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'CommandPort',
        KEY_PATH_ATTR : 'dataType',
        KEY_PATH_ATTRVALUE : 'UNKNOW_TYPE',
        KEY_PATH_SUBTAG : 'mxGeometry',
    }
)
rule.append(
    {
        KEY_RULE_OP : DELETE_SUBTAG,
        KEY_RULE_TAG : 'CommandPort'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'CommandPort',
        KEY_PATH_ATTR : 'dataType',
        KEY_PATH_ATTRVALUE : 'UNKNOW_TYPE',
        KEY_PATH_SUBTAG : 'mxGeometry',
    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB,
        KEY_RULE_ATTR : 'initialState',
        KEY_RULE_VALUE : '-1.0'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink',
        KEY_PATH_SUBTAG : 'mxGeometry',
        KEY_PATH_SUBSUBTAG : 'Array',
    }
)
rule.append(
    {
        KEY_RULE_OP : DELETE_SUBSUB_ATTRIB,
        KEY_RULE_ATTR : 'scilabClass'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'Product',
        KEY_PATH_ATTR : 'value',
        KEY_PATH_ATTRVALUE : '×',
    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB,
        KEY_RULE_ATTR : 'blocktype',
        KEY_RULE_VALUE : 'c'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'BigSom',
        KEY_PATH_ATTR : 'value',
        KEY_PATH_ATTRVALUE : '+',
    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB,
        KEY_RULE_ATTR : 'blocktype',
        KEY_RULE_VALUE : 'c'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'BasicBlock',
    }
)
rule.append(
    {
        KEY_RULE_OP : BLOCK_TYPE_C,
        KEY_RULE_ATTR : 'blockType',
        KEY_RULE_VALUE : 'c'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'AfficheBlock',
    }
)
rule.append(
    {
        KEY_RULE_OP : ADD_ATTRIB,
        KEY_RULE_ATTRIBUTE : {'blockType' : 'c'}
    }
)

path.append(
    {
        KEY_PATH_TAG : 'CommandPort',
    }
)
rule.append(
    {
        KEY_RULE_OP : ADD_ATTRIB,
        KEY_RULE_ATTRIBUTE : {'value' : ''}
    }
)

path.append(
    {
        KEY_PATH_TAG : 'SplitBlock',

    }
)
rule.append(
    {
        KEY_RULE_OP : ADD_ATTRIB,
        KEY_RULE_ATTRIBUTE : {'blockType' : 'c','dependsOnU':"0",'dependsOnT':"0",'interfaceFunctionName':"SPLIT_f", 'simulationFunctionName':""}
        

    }
)

path.append(
    {
        KEY_PATH_TAG :'TextBlock',
        KEY_PATH_SUBTAG :'ScilabString' ,
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'ScilabString',
})
path.append(
    {
        KEY_PATH_TAG :'TextBlock',
        KEY_PATH_SUBTAG :'ScilabString' ,
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'ScilabString',
})

path.append(
    {
        KEY_PATH_TAG : 'TextBlock',
        KEY_PATH_ATTR : 'simulationFunctionType',
        KEY_PATH_ATTRVALUE : 'DEFAULT',
    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB,
        KEY_RULE_ATTR : 'interfaceFunctionName',
        KEY_RULE_VALUE : 'TEXT_f'
    }
)

path.append(
    {
        KEY_PATH_TAG : 'ExplicitInputPort',
        KEY_PATH_ATTR : 'value',
        KEY_PATH_ATTRVALUE : '×'
    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB,
        KEY_RULE_ATTR : 'value',
        KEY_RULE_VALUE : '&#xD7;'
    }
)


path.append(
    {
        KEY_PATH_TAG : 'ExplicitInputPort',
        KEY_PATH_ATTR : 'value',
        KEY_PATH_ATTRVALUE : '÷'
    }
)
rule.append(
    {
        KEY_RULE_OP : REPLACE_ATTRIB,
        KEY_RULE_ATTR : 'value',
        KEY_RULE_VALUE : '&#xF7;'
    }
)

#blocktype=h

#remove all array tags
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'h' ,
        KEY_PATH_SUBTAG :'Array' ,
        
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'Array',
})



#adding superblock and its tag
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'SuperBlockDiagram',
    KEY_RULE_ATTR:{'as':"child",'background':"-1",'gridEnabled':"1",'title':""},
    
})


path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'child'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"context",'scilabClass':"String[]"},
    
})



#adding subtag in array
path.append(
    {

        KEY_PATH_TAG :'SuperBlockDiagram',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'child'
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'Array' ,
    KEY_RULE_SUBATTR : 'as',
    KEY_RULE_SUBATTRVALUE : 'context' ,
    KEY_RULE_TAG:'add',
    KEY_RULE_ATTR:{'value':""},
    
})


#<mxGraphModel as="model">
path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'child'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'mxGraphModel',
    KEY_RULE_ATTR:{'as':"model"},
    
})


#add root in mxgraphmodel
path.append(
    {
        
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'mxGraphModel',
    KEY_RULE_TAG:'root',
    KEY_RULE_ATTR:{},
    
})


#mxCell id="-4b9f829c:15ec1dacbf9:-7e7d"
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
    }
)
rule.append({
    KEY_RULE_OP: BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'mxCell',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbf9:-7e7d"},
    
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
    }
)
rule.append({
    KEY_RULE_OP: BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'mxCell',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbfa:-7e7d",'parent':"-4b9f829c:15ec1dacbf9:-7e7d"}
})

#EventOutBlock id="-4b9f829c:15ec1dacbf8:-7cbf" parent="-4b9f829c:15ec1dacbfa:-7e7d" interfaceFunctionName="CLKOUT_f" blockType="d" dependsOnU="0" dependsOnT="0" simulationFunctionName="output" simulationFunctionType="DEFAULT" style="CLKOUT_f"
#<ControlPort id="-34ccd236:16f5fd166de:-7ffb" parent="-4b9f829c:15ec1dacbf8:-7cbf" ordering="1" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="0.0" style="ControlPort;align=center;verticalAlign=top;spacing=10.0;rotation=90" value=""/>
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'EventOutBlock',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbf8:-7cbf",'parent':"-4b9f829c:15ec1dacbfa:-7e7d",'interfaceFunctionName':"CLKOUT_f",'blockType':"d",'dependsOnU':"0",'dependsOnT':"0",'simulationFunctionName':"output",'simulationFunctionType':"DEFAULT",'style':"CLKOUT_f"},
   
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'ControlPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ffb",'parent':"-4b9f829c:15ec1dacbf8:-7cbf",'ordering':"1",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"0.0",'style':"ControlPort;",'align':'center;','verticalAlign':'top;','spacing':'10.0;','rotation':"90",'value':""}
})


#child nodes in eventblock
path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabString',
    KEY_RULE_ATTR:{'as':"exprs" , 'height':"1" , 'width':"1"},
    
})



path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"realParameters" , 'height':"0" , 'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"integerParameters" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"objectsParameters" , 'scilabClass':"ScilabList"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nbZerosCrossing" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nmode" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"state" , 'height':"0" , 'width':"0"},
    
})



path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"dState" , 'height':"0" , 'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"oDState" , 'scilabClass':"ScilabList"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"equations" , 'scilabClass':"ScilabList"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'mxGeometry',
    KEY_RULE_ATTR:{'as':"geometry" , 'x':"0.0" , 'y':"0.0" , 'width':"20.0" , 'height':"20.0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabString' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"1"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'integerParameters' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"1"},
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'nbZerosCrossing' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'nmode' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0"},
    
})






#BasicBlock id="-4b9f829c:15ec1dacbf8:-7cbd" parent="-4b9f829c:15ec1dacbfa:-7e7d" interfaceFunctionName="EVTDLY_c" blockType="d" dependsOnU="0" dependsOnT="0" simulationFunctionName="evtdly4" simulationFunctionType="C_OR_FORTRAN" style="EVTDLY_c"
#ControlPort id="-34ccd236:16f5fd166de:-7ff9" parent="-4b9f829c:15ec1dacbf8:-7cbd" ordering="1" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="0.0" style="ControlPort;align=center;verticalAlign=top;spacing=10.0;rotation=90" value=""
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'BasicBlock',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbf8:-7cbd",'parent':"-4b9f829c:15ec1dacbfa:-7e7d",'interfaceFunctionName':"EVTDLY_c",'blockType':"d",'dependsOnU':"0",'dependsOnT':"0",'simulationFunctionName':"evtdly4",'simulationFunctionType':"C_OR_FORTRAN",'style':"EVTDLY_c"},
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'ControlPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff9",'parent':"-4b9f829c:15ec1dacbf8:-7cbd",'ordering':"1",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"0.0",'style':"ControlPort;",'align':'center;','verticalAlign':'top;','spacing':'10.0;','rotation':"90",'value':""}
})

# adding subtags in basic block
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabString',
    KEY_RULE_ATTR:{'as':"exprs",'height':"2",'width':"1"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"realParameters",'height':"1",'width':"2"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"integerParameters",'height':"0",'width':"0"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"objectsParameters",'scilabClass':"ScilabList"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nbZerosCrossing",'height':"1",'width':"1",'intPrecision':"sci_int32"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nmode",'height':"1",'width':"1",'intPrecision':"sci_int32"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"state",'height':"0",'width':"0"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"dState",'height':"0",'width':"0"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"oDState",'scilabClass':"ScilabList"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"equations",'scilabClass':"ScilabList"},
    
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'mxGeometry',
    KEY_RULE_ATTR:{'as':"geometry",'x':"0.0",'y':"0.0",'width':"20.0",'height':"20.0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabString' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0.1"},
    
})
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabString' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"1" , 'column':"0" , 'value':"0.1"},
    
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabDouble' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'realParameters' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'realPart':"0.1"},
})
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabDouble' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'realParameters' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"1" , 'realPart':"0.0"},
})

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'nbZerosCrossing' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'EVTDLY_c'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'nmode' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0"},
    
})


#CommandPort id="-34ccd236:16f5fd166de:-7ff8" parent="-4b9f829c:15ec1dacbf8:-7cbd" ordering="1" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="0.1" style="CommandPort;align=center;verticalAlign=bottom;spacing=10.0;rotation=90" value=""
#SplitBlock id="-4b9f829c:15ec1dacbf8:-7cba" parent="-4b9f829c:15ec1dacbfa:-7e7d" interfaceFunctionName="CLKSPLIT_f" blockType="d" dependsOnU="0" dependsOnT="0" simulationFunctionName="split" simulationFunctionType="DEFAULT" style="CLKSPLIT_f"
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'CommandPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff8",'parent':"-4b9f829c:15ec1dacbf8:-7cbd",'ordering':"1",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"0.1",'style':"CommandPort;",'align':'center;','verticalAlign':'bottom;','spacing':'10.0;','rotation':"90",'value':""},
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'SplitBlock',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbf8:-7cba",'parent':"-4b9f829c:15ec1dacbfa:-7e7d",'interfaceFunctionName':"CLKSPLIT_f",'blockType':"d",'dependsOnU':"0",'dependsOnT':"0",'simulationFunctionName':"split",'simulationFunctionType':"DEFAULT",'style':"CLKSPLIT_f"}
})


#split
path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"exprs",'height':"0",'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"realParameters",'height':"0",'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"integerParameters",'height':"0",'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"objectsParameters",'scilabClass':"ScilabList"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"state",'height':"0",'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':"dState",'height':"0",'width':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"oDState",'scilabClass':"ScilabList"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"equations",'scilabClass':"ScilabList"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'mxGeometry',
    KEY_RULE_ATTR:{'as':"geometry",'x':"0.0",'y':"0.0",'width':"7.0",'height':"7.0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nbZerosCrossing" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nmode" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'nbZerosCrossing' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0"},
    
})


path.append(
    {
        KEY_PATH_TAG :'SplitBlock',
        KEY_PATH_ATTR : 'style' ,
        KEY_PATH_ATTRVALUE : 'CLKSPLIT_f'
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'ScilabInteger' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'nmode' ,
    KEY_RULE_TAG:'',
    KEY_RULE_ATTR:{'data line':"0" , 'column':"0" , 'value':"0"},
    
})


#<ControlPort id="-34ccd236:16f5fd166de:-7ff6" parent="-4b9f829c:15ec1dacbf8:-7cba" ordering="1" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="0.0" style="ControlPort;align=center;verticalAlign=top;spacing=10.0;rotation=90" value=""/>
#<CommandPort id="-34ccd236:16f5fd166de:-7ff5" parent="-4b9f829c:15ec1dacbf8:-7cba" ordering="1" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="-1.0" style="CommandPort;align=center;verticalAlign=bottom;spacing=10.0;rotation=90" value=""/>
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'ControlPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff6",'parent':"-4b9f829c:15ec1dacbf8:-7cba",'ordering':"1",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"0.0",'style':"ControlPort;",'align':'center;','verticalAlign':'top;','spacing':'10.0;','rotation':"90",'value':""},
}) 


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'CommandPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff5",'parent':"-4b9f829c:15ec1dacbf8:-7cba",'ordering':"1",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"-1.0",'style':"CommandPort;",'align':'center;','verticalAlign':'bottom;','spacing':'10.0;','rotation':"90",'value':""}
})

#<CommandPort id="-34ccd236:16f5fd166de:-7ff4" parent="-4b9f829c:15ec1dacbf8:-7cba" ordering="2" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="-1.0" style="CommandPort;align=center;verticalAlign=bottom;spacing=10.0;rotation=90" value=""/>
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'CommandPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff4",'parent':"-4b9f829c:15ec1dacbf8:-7cba",'ordering':"2",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"-1.0",'style':"CommandPort;",'align':'center;','verticalAlign':'bottom;','spacing':'10.0;','rotation':"90",'value':""},
})

#1. <CommandControlLink id="-34ccd236:16f5fd166de:-7ff3" parent="-4b9f829c:15ec1dacbfa:-7e7d" source="-34ccd236:16f5fd166de:-7ff4" target="-34ccd236:16f5fd166de:-7ff9" style="CommandControlLink" value="">

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'CommandControlLink',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff3",'parent':"-4b9f829c:15ec1dacbfa:-7e7d",'source':"-34ccd236:16f5fd166de:-7ff4",'target':"-34ccd236:16f5fd166de:-7ff9",'style':"CommandControlLink",'value':""}
})


#mxGeometry
path.append(
    {
        
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'CommandControlLink' ,
    KEY_RULE_TAG:'mxGeometry',
    KEY_RULE_ATTR:{'as':"geometry"},
    
})

#mxPoint as="sourcePoint" x="0.0" y="11.0"
path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'mxGeometry' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'geometry' ,
    KEY_RULE_TAG:'mxPoint',
    KEY_RULE_ATTR:{'as':"sourcePoint",'x':"0.0",'y':"11.0"},
    
})


path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'mxGeometry' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'geometry' ,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"points"},
    
})


path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'Array' ,
    KEY_RULE_TAG:'mxPoint',
    KEY_RULE_ATTR:{'x':"380.71" , 'y':"290.0"},
    
})


path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'Array' ,
    KEY_RULE_TAG:'mxPoint',
    KEY_RULE_ATTR:{'x':"340.0" , 'y':"290.0"},
    
})




#mxPoint as="targetPoint" x="10.0" y="-4.0"
path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'mxGeometry' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'geometry' ,
    KEY_RULE_TAG:'mxPoint',
    KEY_RULE_ATTR:{'as':"targetPoint",'x':"20.0",'y':"-4.0"},
    
})


#2. <CommandControlLink id="-34ccd236:16f5fd166de:-7ff2" parent="-4b9f829c:15ec1dacbfa:-7e7d" source="-34ccd236:16f5fd166de:-7ff5" target="-34ccd236:16f5fd166de:-7ffb" style="CommandControlLink" value="">

path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_PATH_ATTRVALUE : 'h' ,
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG :'root',
    KEY_RULE_TAG:'CommandControlLink',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ff2" , 'parent':"-4b9f829c:15ec1dacbfa:-7e7d" , 'source':"-34ccd236:16f5fd166de:-7ff5" , 'target':"-34ccd236:16f5fd166de:-7ffb" , 'style':"CommandControlLink" , 'value':""}
})


#mxGeometry
path.append(
    {
        
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'mxGeometry',
    KEY_RULE_ATTR:{'as':"geometry"},
    
})



#mxPoint as="sourcePoint" x="0.0" y="11.0"
path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'mxGeometry' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'geometry' ,
    KEY_RULE_TAG:'mxPoint',
    KEY_RULE_ATTR:{'as':"sourcePoint",'x':"0.0",'y':"11.0"},
    
})


#mxPoint as="targetPoint" x="10.0" y="-4.0"
path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'mxGeometry' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'geometry' ,
    KEY_RULE_TAG:'mxPoint',
    KEY_RULE_ATTR:{'as':"targetPoint",'x':"10.0",'y':"-4.0"},
    
}) 


path.append(
    {
        KEY_PATH_TAG : 'CommandControlLink' ,
        KEY_PATH_ATTR : 'style',
        KEY_RULE_ATTRVALUE :'CommandControlLink',
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_SUBTAG : 'mxGeometry' ,
    KEY_RULE_SUBATTR : 'as' ,
    KEY_RULE_SUBATTRVALUE : 'geometry' ,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"points"},
    
})




#<mxCell as="defaultParent" id="-4b9f829c:15ec1dacbfa:-7e7d" parent="-4b9f829c:15ec1dacbf9:-7e7d"/>
path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
        
 
    }
)
rule.append({
    KEY_RULE_OP:BLOCK_TYPE_H,
    KEY_RULE_TAG:'mxCell',
    KEY_RULE_ATTR:{'as':"defaultParent",'id':"-4b9f829c:15ec1dacbfa:-7e7d",'parent':"-4b9f829c:15ec1dacbf9:-7e7d"},
    
})


#blocktype h
path.append(
    {
        KEY_PATH_TAG : 'BasicBlock',
        KEY_PATH_ATTR : 'blockType',
        KEY_RULE_ATTRVALUE :'h',
    }
)
rule.append({
    KEY_RULE_OP : BLOCK_TYPE_H,
    KEY_RULE_TAG : 'ScilabDouble',
    KEY_RULE_ATTR : {'as':"realParameters",'height':'0','width':'0'}


})

