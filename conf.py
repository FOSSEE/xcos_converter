path = [
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'integerParameters'
    },
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'nmode'
    },
    {
        'tag': 'ScilabDouble',
        'attr': 'as',
        'attrvalue': 'nbZerosCrossing'
    }
]

exp = [
        
        {
            'tag' : 'ExplicitOutPutPort'
        },
        {
            'tag' : 'ExplicitInputPort'
        }
        
]
replacement = [

        {
            'tag': 'ScilabDouble',
            'attr': 'as',
            'attrvalue': 'integerParameters'
        }

]
#rule for changing node based on name
attr=['nmode','nbZerosCrossing','integerParameters']
rules = {"ScilabDouble":"ScilabInteger"}

#setting new attrib
at=['nmode','nbZerosCrossing','integerParameters']
a=["intPrecision"]
b=["sci_int32"]

#removing nodes
ls=[]

#changing existing attribute values
lst = ['realPart']
t = ['value']



#to do
tags  = []

'''attrs = {'as':'exprs'}
newvalue = 'newvalue'
av = {attrs:newvalue}
tags.append({'ScilabString':av})

attrs = {'height':'1'}
newvalue = '2'
av = {attrs:newvalue}
tags.append({'ScilabDouble':av})'''

