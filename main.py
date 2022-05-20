f=open('data/factbook.csv','r')
print(f.read())

f1=open('data/factbook-2.csv','r')
print(f1.read())

with open('data/factbook.csv','r') as f:
    with open('temp/temp.csv','w',newline='') as fp:
        rf=f.readlines()
        seen = set()
        for i in rf:
            if i in seen:
                continue
            seen.add(i)
            fp.write(i)

with open('data/factbook-2.csv','r') as f1:
    with open('temp/temp.csv','a',newline='') as fp:
        rf=f1.readlines()
        seen = set()
        for i in rf:
            if i in seen:
                continue
            seen.add(i)
            fp.write(i)
with open('temp/temp.csv','r') as f:
    with open('output/output.csv','w',newline='') as fp:
        rf=f.readlines()
        seen=set()
        for i in rf:
            if i in seen:
                continue
            seen.add(i)
            if i.split("\n"):
                fp.write("\n")
            fp.write(str(i.split(';')))
