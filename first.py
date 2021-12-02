st = 'My first git-repo'
for i in st[::-1]:
    st += i
st = st[len(st)//2:]
for i in st[::-1]:
    st += i
st = st[len(st)//2:]
for i in st[::-1]:
    st += i
st = st[len(st)//2:]
for i in st[::-1]:
    st += i
st = st[len(st)//2:]
for i in st[::-1][::-1]:
    print(i, end='')