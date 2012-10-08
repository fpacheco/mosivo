#!/usr/bin/python2

r = open('Planes.csv','r')
s = open('Planes.modif','w')

for line in r:    
    mArray = line.split('|')
    if ('##' in mArray[2]):
        tmp = mArray[2]
        nA = tmp.split(',')
        nA[1]=nA[1].strip()
        nA[2]=nA[2].strip()
        if int(nA[1])<10:
            nA[1]='0%s' % nA[1]
        if int(nA[2])<10:
            nA[2]='0%s' % nA[2]
        nE = '%s-%s-%s' % ( nA[0][2:6],nA[1],nA[2] )
        mArray[2] = nE

    nline = '|'.join(mArray)
    s.write(nline)

s.close()
r.close()
