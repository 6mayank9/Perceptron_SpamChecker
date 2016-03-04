import operator
import random

def dot(vector1,vector2):
   #value = sum(map( operator.mul, vector1, vector2))
   #return value
   value = 0
   for x in range(126):
       value+= (vector1[x]*vector2[x])
   return value
def extractFvalues(featureExtract,y):
    featureValue = [0 for x in range(126)]
    i=0

    for x in range(0,126):
        str = "".join(featureExtract[y][i])
        str = str.split(":")
        if((float(str[0])-1) == float(x)):
           featureValue[x] = float(str[1])
           i+=1
        if(i>=len(featureExtract[y])):
            break
    return featureValue

def test(b,w,featureValue):
    y = b + dot(w,featureValue)

    if y>0:
        y = 1
    elif y<0:
        y = -1
    return y




data = open("data.svm")
trueLabel = {}
i=0
str = []

featureExtract = [[0 for x in range(126)] for x in range(350000)]
for row in data :
   trueLabel[i] = float(row.split()[0])
   featureExtract[i] = row.split()[1:]
   i+=1


#featureValue = extractFvalues(featureExtract,0)    //extract feature values
trainData = random.sample(range(0, 350000), 250000)


w = [0 for x in range(126)]
k = 0
b = 0 # b???
T=0
count = 0
while(T<20):
    for k in trainData:


        featureValue = extractFvalues(featureExtract,k)
        #print featureValue
        #print trueLabel[k]
        #print b
        #raw_input()
        if(test(b,w,featureValue)!= trueLabel[k]):

            if(trueLabel[k] == 1):
                w = [w_i + x_i for w_i,x_i in zip(w,featureValue) ]
            else:
                w = [w_i - x_i for w_i,x_i in zip(w,featureValue) ]
            #l = [trueLabel[k]*x for x in featureValue] # wi * xi
            #print l
            #w = [sum(x) for x in zip(*[w,l])] # wNew
            #print w
            b = b + trueLabel[k]  # bNew
            #print b
            #raw_input()


        #count+=1
        #if count >= 10000:
        #    T+=1

        #if T==2:
         #   break

        #print count

    T+=1
    a=0
    co=0
    ac=0
    print 'testing'
    while(1):
     if a not in trainData:
      featureValue = extractFvalues(featureExtract,a)
      if(test(b,w,featureValue)== trueLabel[a]):
        ac+=1 # Accuracy

      co+=1
     #print co
     a+=1
     if(co%1000==0):
         print co
     if co>=50000:
      break
    print 'T=',T,' accuracy = ',ac
