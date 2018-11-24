


class SimFileError(Exception):
    def __init__(self,message):
        super().__init__(message)
    def event(self,gameid,eid,evt):
        self.args = ('\n'.join(self.args+(f'Event [{gameid}]-[{eid}] ({evt})',)),)
        return self
    def add(self,head,data):
        self.args = ('\n'.join(self.args+('%s [%s]'%(head,data),)),)
        return self

def list_extract(v,l):
    if type(v)==list:
        for i,x in enumerate(l):
            if x in v:break
        else:
            return None,l
    else:
        for i,x in enumerate(l):
            if x==v:break
        else:
            return None,l
    return x,l[:i]+l[i+1:]

def split_paren(s):
    while len(s)>0:
        j = s.find(')',1)
        yield s[1:j]
        s = s[j+1:]

def charmerge_set(a,b):
    i,j,A,B = 0,0,len(a),len(b)
    while i<A and j<B:
        if a[i]<b[j]:
            yield a[i]
            i=i+1
        elif a[i]>b[j]:
            yield b[j]
            j=j+1
        else:
            yield a[i]
            i,j=i+1,j+1
    if i<A:
        yield a[i:]
    elif j<B:
        yield b[j:]

def charmerge_list(a,b):
    i,j,A,B = 0,0,len(a),len(b)
    while i<A and j<B:
        if a[i]<b[j]:
            yield a[i]
            i=i+1
        elif a[i]>b[j]:
            yield b[j]
            j=j+1
        else:
            yield a[i]+b[j]
            i,j=i+1,j+1
    if i<A:
        yield a[i:]
    elif j<B:
        yield b[j:]


def charsort_set(l):
    if len(l)<=1:
        if len(l)==1: yield l
        return
    m = len(l)//2
    a,b = ''.join(charsort_set(l[:m])),''.join(charsort_set(l[m:]))
    i,j,A,B = 0,0,len(a),len(b)
    while i<A and j<B:
        if a[i]<b[j]:
            yield a[i]
            i=i+1
        elif a[i]>b[j]:
            yield b[j]
            j=j+1
        else:
            yield a[i]
            i,j=i+1,j+1
    if i<A:
        yield a[i:]
    elif j<B:
        yield b[j:]

def charsort_list(l):
    if len(l)<=1:
        if len(l)==1: yield l
        return
    m = len(l)//2
    a,b = ''.join(charsort_list(l[:m])),''.join(charsort_list(l[m:]))
    i,j,A,B = 0,0,m,m+len(l)%2
    while i<A and j<B:
        if a[i]<b[j]:
            yield a[i]
            i=i+1
        elif a[i]>b[j]:
            yield b[j]
            j=j+1
        else:
            yield a[i]+b[j]
            i,j=i+1,j+1
    if i<A:
        yield a[i:]
    elif j<B:
        yield b[j:]



## pyutil.search

def binaryIndex(a,v,l=0,r=None):
    if r==None: r=len(a)
    while l<r:
        m=(l+r)//2
        if v > a[m]:
            l = m+1
        elif v < a[m]:
            r = m
        else:
            return m
    return None


## pyutil.multisort

def _mergesort_index(fn):
    def wrapper(inx,data):
        if len(inx)<=1:
            return inx
        m = len(inx)//2
        l = wrapper(inx[:m],data)
        r = wrapper(inx[m:],data)
        return [*fn(l,r,data)]
    return wrapper

@_mergesort_index
def _multisortLvl(a,b,data):
    i,j,x,y = 0,0,len(a),len(b)
    while i<x and j<y:
        if data[a[i][0]] < data[b[j][0]]:
            yield a[i]
            i=i+1
        elif data[a[i][0]] > data[b[j][0]]:
            yield b[j]
            j=j+1
        else:
            yield a[i]+b[j]
            i,j=i+1,j+1
    while i<x:
        yield a[i]
        i=i+1
    while j < y:
        yield b[j]
        j=j+1


def _multisort_algorithm(fn):
    def multisort(inx,data):
        if len(data)==1:
            return fn(inx,data[0])
        lvl = _multisortLvl([[x] for x in inx],data[0])
        return [a for b in [multisort(x,data[1:]) if len(x)>1 else x for x in lvl] for a in b]

    def wrapper(data):
        m = max(len(x) for x in data)
        inx = multisort([*range(m)],data)
        return [[x[i] for i in inx] for x in data]
    return wrapper


@_multisort_algorithm
def multisortSet(inx,data):
    lvl = _multisortLvl([[x] for x in inx],data)
    return [min(x) for x in lvl]
