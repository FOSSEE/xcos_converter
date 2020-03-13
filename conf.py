DOUBLE_TO_INTEGER = 1
DELETE_ATTRIB = 2
MAIN_BLOCK = 3
ADD_SUB_SUBTAG = 4
DELETE_SUBTAG = 5
DOUBLE_TO_INTEGER_AND_SWAP = 6
DELETE_SUB_ATTRIB = 7
DELETE_SUBSUB_ATTRIB = 8
ADD_ATTRIB = 9

path = []
rule = []


path.append(
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'nmode',
        'subtag':'data',
        'subattr':'realPart'
    })
rule.append({
    'op':DOUBLE_TO_INTEGER,
    'tag':'ScilabInteger',
    'attribute':{'intPrecision':'sci_int32'},
    'attr':'value'
})



path.append(    
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'nbZerosCrossing',
        'subtag':'data',
        'subattr':'realPart'
    })
rule.append({
    'op':DOUBLE_TO_INTEGER,
    'tag':'ScilabInteger',
    'attribute':{'intPrecision':'sci_int32'},
    'attr':'value'
})



path.append(
    {
        'tag':'BasicBlock',
        
    })
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering'
})

path.append(
    {
        'tag':'BasicBlock',
        
    })
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})

path.append(
    {
        'tag':'BasicBlock',
        
    })
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})



path.append(
    {
        'tag':'Product',
        
    })
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering'
})

path.append(
    {
        'tag':'Product',
        
    })
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})

path.append(
    {
        'tag':'Product',
        
    })
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})


path.append(
    {
        'tag':'BigSom',
        
    })
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering',
})

path.append(
    {
        'tag':'BigSom',
        
    })
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})

path.append(
    {
        'tag':'BigSom',
        
    })
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})



path.append(
    {
        'tag':'AfficheBlock',
        
    }
)
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering',
})
path.append(
    {
        'tag':'AfficheBlock',
        
    }
)
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})

path.append(
    {
        'tag':'AfficheBlock',
        
    }
)
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'},
    'attribute':{'dependsOnT' : '0'},
    'attr1' : 'dependsOnU',
    'value' : '0'
})



path.append(
    {
        'tag':'ExplicitLink',
        'subtag':'mxGeometry',
    }
)
rule.append({
    'op':DELETE_SUB_ATTRIB,
    'attr':'y',
})

path.append(
    {
        'tag':'ExplicitLink',
        'subtag':'mxGeometry',
 
    }
)
rule.append({
    'op':ADD_SUB_SUBTAG,
    'subsubtag':'mxPoint',
    'attr':{'as':'sourcePoint','x':'0.0','y':'0.0'},
    'subsubtag1':'mxPoint',
    'attr1':{'as':'targetPoint','x':'0.0','y':'0.0'}
})


path.append(
    {
        'tag':'ExplicitLink',
        'subtag':'mxGeometry',
        'subsubtag':'Array',
    }
)
rule.append({
    'op':DELETE_SUBSUB_ATTRIB,
    'attr':'scilabClass',
})



path.append(
    {
        'tag':'ExplicitInputPort',
        'subtag':'mxGeometry' ,
    })
rule.append({
    'op':DELETE_SUBTAG,
    'subtag':'mxGeometry',
})

path.append(
    {
        'tag':'ExplicitInputPort',
        
    })
rule.append({
    'op':ADD_ATTRIB,
    'attribute':{'initialState':'-1.0'},
    'attr' : 'dataLines',
    'value' : "-1"
})

path.append(
    {
        'tag':'ExplicitOutputPort',
        'subtag':'mxGeometry' ,
    })
rule.append({
    'op':DELETE_SUBTAG,
    'subtag':'mxGeometry',
})

path.append(
    {
        'tag':'ExplicitOutputPort',
        
    })
rule.append({
    'op':ADD_ATTRIB,
    'attribute':{'initialState':'-1.0'},
    'attr' : 'dataLines',
    'value' : "-1"
})


path.append(
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'integerParameters',
        'subtag':'data',
        'subattr':'realPart'
    })
rule.append({
    'op':DOUBLE_TO_INTEGER_AND_SWAP,
    'tag':'ScilabInteger',  
    'attribute':{'intPrecision':'sci_int32'},
    'attr':'value'
})

