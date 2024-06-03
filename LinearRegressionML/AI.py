import functions as fn

with open("dataToFeedX.txt") as dtfx:
    dtfx=dtfx.readlines()

with open("dataToFeedY.txt") as dtfy:
    dtfy=dtfy.readlines()

dataX=fn.dataSorting(dtfx) 
dataY=fn.dataSorting(dtfy)

# print(dataX,dataY)

m=fn.covar(dataX,dataY)/fn.var(dataX)

c=fn.exp(dataY)-fn.exp(dataX)*m

dataToTest=int(input("Enter your data: "))
y=m*dataToTest+c
print(f"Your output is: {y}")
