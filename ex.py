#C:\Users\schul_000\Documents\GitHub\projekty\ex.py

l = []
for i in range(1000,3001):
    c = 0
    for j in str(i):
        if int(j)%2!=0:
            c+=1
    if c==4:
        l.append(str(i))
print " ".join(l)
