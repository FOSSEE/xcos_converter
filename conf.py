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
BLOCK_TYPE_H = 15
KEY_RULE_OP = 'op'
KEY_RULE_TAG = 'tag'
KEY_RULE_ATTRIBUTE = 'attribute'
KEY_RULE_ATTR = 'attr'
KEY_RULE_VALUE = 'value'
KEY_RULE_ATTR1 = 'attr1'
KEY_RULE_ATTRVALUE = 'attrvalue'
KEY_RULE_SUBTAG = 'subtag'
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
    KEY_RULE_ATTR : 'dataLines',
    KEY_RULE_VALUE : "-1"
})

path.append(
    {
        KEY_PATH_TAG :'ExplicitInputPort',
        KEY_RULE_ATTR : 'dataType',
        KEY_RULE_ATTRVALUE : 'REAL_MATRIX',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTR : 'dataColumns',
    KEY_RULE_VALUE: "-2"
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
    KEY_RULE_ATTR : 'dataLines',
    KEY_RULE_VALUE: "-1"
})

path.append(
    {
        KEY_PATH_TAG :'ExplicitOutputPort',
        KEY_RULE_ATTR : 'dataType',
        KEY_RULE_ATTRVALUE : 'REAL_MATRIX',
        
    })
rule.append({
    KEY_RULE_OP:ADD_ATTRIB,
    KEY_RULE_ATTR : 'dataColumns',
    KEY_RULE_VALUE: "-2"
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
path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
        KEY_PATH_SUBTAG :'Array' ,
        
    })
rule.append({
    KEY_RULE_OP:DELETE_SUBTAG,
    KEY_RULE_SUBTAG:'Array',
})


path.append(
    {
        KEY_PATH_TAG :'BasicBlock',
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'SuperBlockDiagram',
    KEY_RULE_ATTR:{'as':"child",'background':"-1",'gridEnabled':"1",'title':""},
    
})

#super
path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'Array',
    KEY_RULE_ATTR:{'as':"context",'scilabClass':"String[]"},
    
})

#<add value=""/>

#<mxGraphModel as="model">
path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'mxGraphModel',
    KEY_RULE_ATTR:{'as':"model"},
    
})

#mxCell id="-4b9f829c:15ec1dacbf9:-7e7d"
path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
        KEY_PATH_SUBTAG :'mxGraphModel',
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_SUB_SUBTAG,
    KEY_RULE_SUBSUBTAG:'mxCell',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbf9:-7e7d"},
    KEY_RULE_SUBSUBTAG1:'mxCell',
    KEY_RULE_ATTR1:{'id':"-4b9f829c:15ec1dacbfa:-7e7d",'parent':"-4b9f829c:15ec1dacbf9:-7e7d"}
})

#EventOutBlock id="-4b9f829c:15ec1dacbf8:-7cbf" parent="-4b9f829c:15ec1dacbfa:-7e7d" interfaceFunctionName="CLKOUT_f" blockType="d" dependsOnU="0" dependsOnT="0" simulationFunctionName="output" simulationFunctionType="DEFAULT" style="CLKOUT_f"
#<ControlPort id="-34ccd236:16f5fd166de:-7ffb" parent="-4b9f829c:15ec1dacbf8:-7cbf" ordering="1" dataType="REAL_MATRIX" dataColumns="1" dataLines="-1" initialState="0.0" style="ControlPort;align=center;verticalAlign=top;spacing=10.0;rotation=90" value=""/>
path.append(
    {
        KEY_PATH_TAG :'mxGraphModel',
        KEY_PATH_ATTR :'as',
        KEY_PATH_ATTRVALUE : 'model'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'EventOutBlock',
    KEY_RULE_ATTR:{'id':"-4b9f829c:15ec1dacbf8:-7cbf",'parent':"-4b9f829c:15ec1dacbfa:-7e7d",'interfaceFunctionName':"CLKOUT_f",'blockType':"d",'dependsOnU':"0",'dependsOnT':"0",'simulationFunctionName':"output",'simulationFunctionType':"DEFAULT",'style':"CLKOUT_f"},
})


path.append(
    {
        KEY_PATH_TAG :'mxGraphModel',
        KEY_PATH_ATTR :'as',
        KEY_PATH_ATTRVALUE : 'model'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ControlPort',
    KEY_RULE_ATTR:{'id':"-34ccd236:16f5fd166de:-7ffb",'parent':"-4b9f829c:15ec1dacbf8:-7cbf",'ordering':"1",'dataType':"REAL_MATRIX",'dataColumns':"1",'dataLines':"-1",'initialState':"0.0",'style':"ControlPort;",'align':'center;','verticalAlign':'top;','spacing':'10.0;','rotation':"90",'value':""}
})

#<mxCell as="defaultParent" id="-4b9f829c:15ec1dacbfa:-7e7d" parent="-4b9f829c:15ec1dacbf9:-7e7d"/>
path.append(
    {
        KEY_PATH_TAG :'SuperBlockDiagram',
        
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
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


path.append(
    {
        KEY_PATH_TAG :'Array',
        KEY_PATH_ATTR : 'scilabClass' ,
        KEY_PATH_ATTRVALUE : 'String[]'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'add',
    KEY_RULE_ATTR:{'value':""},
    
})


path.append(
    {
        KEY_PATH_TAG :'EventOutBlock',
        KEY_PATH_ATTR : 'blockType' ,
        KEY_PATH_ATTRVALUE : 'd'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ScilabString',
    KEY_RULE_ATTR:{'as':"exprs" , 'height':"1" , 'width':"1"},
    
})


path.append(
    {
        KEY_PATH_TAG :'ScilabString',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'exprs'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"integerParameters" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'ScilabInteger',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'integerParameters'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nbZerosCrossing" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'ScilabInteger',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'nbZerosCrossing'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'ScilabInteger',
    KEY_RULE_ATTR:{'as':"nmode" , 'height':"1" , 'width':"1" , 'intPrecision':"sci_int32"},
    
})


path.append(
    {
        KEY_PATH_TAG :'ScilabInteger',
        KEY_PATH_ATTR : 'as' ,
        KEY_PATH_ATTRVALUE : 'nmode'
 
    }
)
rule.append({
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
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
    KEY_RULE_OP:ADD_TAG,
    KEY_RULE_TAG:'mxGeometry',
    KEY_RULE_ATTR:{'as':"geometry" , 'x':"0.0" , 'y':"0.0" , 'width':"20.0" , 'height':"20.0"},
    
})