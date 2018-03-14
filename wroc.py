import re
def f1(a,b=0):
    return a*a+b

def f2(a):
    if a:
        return a[0]
    else:
        return "BUUUUM"

def f3(a):
    if a==1:
        return "jeden"
    elif a==2:
        return "dwa"
    elif a==3:
        return "trzy"
    else:
        return "other"

def f4(a,b=""):
    if b:
        return "%s ma kota i %s" %(a,b)
    else:
        return "%s ma kota" %a

def f5(a,b=""):
    if a==0:
        return []
    elif b:
        return range(a)[::b]
    else:
        return range(a)

def f6(a,b):
    return a*b

def f7(a):
    if re.match("[aA-zZ]+",a):
        if len(a.split(' '))==1:
            return "slowo"
        else:
            return "zdanie"
    elif re.match("[0-9]+",a):
        if len(a)==1:
            return "cyfra"
        else:
            return "liczba"
    elif re.match("-",a):
        return "liczba ze znakiem"
#    elif re.match("[A-Z+]",a):
#        return "zdanie"
    elif re.match("<.....>",a):
        return "tag poczatkowy"
    elif re.match("</.....>",a):
        return "tag koncowy"

# testowanie git
