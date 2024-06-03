def pow(m,n):
    s=1
    for i in range(n):
        s=s*m
        i=i+1
    return s
# print(pow(2,3))

def exp(X):
    s=0
    for x in X:
        s=s+x
    s=s/len(X)
    return s

# print(exp([1,2,3,4,5]))

def var(X):
    s=0
    for x in X:
        s=s+x*x
    s=s/len(X)
    s=s-pow(exp(X),2)
    return s
    

# print(var([1,2,3]))

def covar(X,Y):
    s=0
    for (x,y) in zip(X,Y):
        s=s+x*y
    s=s/len(X)
    s=s-exp(X)*exp(Y)
    return s
    

# print(covar([1,2,3],[2,3,4]))
# print(exp([2,3,4]))

def dataSorting(datafile):
    dtfTemp=[]
    for data in datafile:
        data=data.strip()
        data=data.split(",")
        dataTemp=[]
        dtfTemp=dtfTemp+data
    datafile=dtfTemp
    dtfTemp=[]
    for data in datafile:
        dtfTemp.append(float(data))
    datafile=dtfTemp

    return datafile