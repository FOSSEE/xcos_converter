DOUBLE_TO_INTEGER = 1
CHANGE_ATTRIB = 2
DELETE_ATTRIB = 3
MAIN_BLOCK = 4
ADD_SUB_SUBTAG = 5
DELETE_SUBTAG = 6
DOUBLE_TO_INTEGER_AND_SWAP = 7

path = []
rule = []


path.append(
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'nmode'
    })
rule.append({
    'op':DOUBLE_TO_INTEGER,
    'tag':'ScilabInteger',
    'attribute':{'intPrecision':'sci_int32'}
})

path.append(
    {
        'tag': 'ScilabDouble',
        'subtag':'data',
        'attr':'realPart'
    })
rule.append({
    'op':CHANGE_ATTRIB,
    'attr':'value'
})



path.append(    
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'nbZerosCrossing'
    })
rule.append({
    'op':DOUBLE_TO_INTEGER,
    'tag':'ScilabInteger',
    'attribute':{'intPrecision':'sci_int32'}
})

path.append(
    {
        'tag': 'ScilabDouble',
        'subtag':'data',
        'attr':'realPart'
    })
rule.append({
    'op':CHANGE_ATTRIB,
    'attr':'value'
})



path.append(
    {
        'tag':'BasicBlock',
        'attr':'ordering',
    })
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering'
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'}
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'}
})



path.append(
    {
        'tag':'Product',
        'attr':'ordering',
    })
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering'
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'}
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'}
})



path.append(
    {
        'tag':'BigSom',
        'attr':'ordering',
    })
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering',
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'}
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'}
})



path.append(
    {
        'tag':'AfficheBlock',
        'attr':'ordering',
    }
)
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'ordering',
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'state','height':'0','width':'0'}
})
rule.append({
    'op':MAIN_BLOCK,
    'tag':'ScilabDouble',
    'attr':{'as':'dState','height':'0','width':'0'}
})



path.append(
    {
        'tag':'ExplicitLink',
        'subtag':'mxGeometry',
        'attr':'y',
    }
)
rule.append({
    'op':DELETE_ATTRIB,
    'attr':'y',
})
rule.append({
    'op':ADD_SUB_SUBTAG,
    'subsubtag':'mxGeometry',
    'attr':{'as':'sourcePoint','x':'0.0','y':'0.0'}
})
rule.append({
    'op':ADD_SUB_SUBTAG,
    'subsubtag':'mxGeometry',
    'attr':{'as':'targetPoint','x':'0.0','y':'0.0'}
})

path.append(
    {
        'tag':'ExplicitLink',
        'subtag':'mxGeometry',
        'subsubtag':'Array',
        'attr':'scilabClass',
    }
)
rule.append({
    'op':DELETE_ATTRIB,
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
        'tag':'ExplicitOutputPort',
        'subtag':'mxGeometry' ,
    })
rule.append({
    'op':DELETE_SUBTAG,
    'subtag':'mxGeometry',
})



path.append(
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'integerParameters'
    })
rule.append({
    'op':DOUBLE_TO_INTEGER_AND_SWAP,
    'tag':'ScilabInteger',  
    'attribute':{'intPrecision':'sci_int32'}
})

path.append(
    {
        'tag': 'ScilabDouble',
        'subtag':'data',
        'attr':'realPart'
    })
rule.append({
    'op':CHANGE_ATTRIB,
    'attr':'value'
})


print(rule)