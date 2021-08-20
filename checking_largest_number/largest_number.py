large=None
print('before')
for a in [4,3,7,39,8]:
    if large is None:
        large=a
    elif large<a:
        large=a    
    print(large,a)
print('After',large)

