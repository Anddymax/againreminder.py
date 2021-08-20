import re
a="aniket shisode@geca"
bx=input('Enter letter you want to find:')
b=re.search(bx,a)               #methods to find letter/s using re keywords

bnn=str(b)
bn=bnn.find('(')
bn2=bnn.find(')')
if b==None:
    print('Match not found!')
else:
    print("position of ",bx,"is",bnn[bn:bn2+1])
