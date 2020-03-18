DOUBLE_TO_INTEGER = 1
DELETE_ATTRIB = 2
MAIN_BLOCK = 3
ADD_SUB_SUBTAG = 4
DELETE_SUBTAG = 5
DOUBLE_TO_INTEGER_AND_SWAP = 6
DELETE_SUB_ATTRIB = 7
DELETE_SUBSUB_ATTRIB = 8
ADD_ATTRIB = 9
KEY_RULE_OP = 'op'
KEY_RULE_TAG = 'tag'
KEY_RULE_ATTRIBUTE = 'attribute'
KEY_RULE_ATTR = 'attr'
KEY_RULE_VALUE = 'value'
KEY_RULE_ATTR1 = 'attr1'
KEY_RULE_SUBTAG = 'subtag'
KEY_RULE_SUBSUBTAG = 'subsubtag'
KEY_RULE_SUBSUBTAG1 = 'subsubtag1'
KEY_PATH_TAG = 'tag'
KEY_PATH_ATTR = 'attr'
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
        KEY_PATH_TAG :'AfficheBlock',
        
    }
)
rule.append({
    KEY_RULE_OP:MAIN_BLOCK,
    KEY_RULE_TAG:'ScilabDouble',
    KEY_RULE_ATTR:{'as':'dState','height':'0','width':'0'},
    KEY_RULE_ATTRIBUTE:{'dependsOnT' : '0'},
    KEY_RULE_ATTR1 : 'dependsOnU',
    KEY_RULE_VALUE : '0'
})



path.append(
    {
        KEY_PATH_TAG :'ExplicitLink',
        KEY_PATH_SUBTAG :'mxGeometry',
    }
)
rule.append({
    KEY_RULE_OP:DELETE_SUB_ATTRIB,
    KEY_RULE_ATTR:'y',
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

