# variable declaration
#TEST CASE
n = 3
M = 2.0
B = 1.0
wt = [[0.3,0.6,0.7],[0.6,0.7,0.8],[0.5,0.7,0.8]]
wm = [[0.1,0.2,0.3],[0.3,0.4,0.4],[0.2,0.3,0.6]]
csl=[0,0,0]
cost=[]
QoS=[[2,4,5],[4,7,8],[2,6,7]]
APU=0
ABU=0


#updating M,B to minimum resources
for i in range(n):
  M=M-wt[i][0]
  B=B-wm[i][0]


#finding alpha
for i in range(n):
  APU+=(sum(wt[i])/len(wt[i]))
  ABU+=(sum(wm[i])/len(wm[i]))

APU=APU/M
ABU=ABU/B
a=ABU/(ABU+APU)

#Cost functions
def dQoS(i,j,k):

  return QoS[i][k]-QoS[i][j]

def dCR(i,j,k):
  res=(1-a)*(wt[i][k]-wt[i][j])
  res+=a*(wm[i][k]-wm[i][j])
  return res

def ComputeCost():
  for i in range(n):
    x=len(wt[i])-1
    if csl[i]<x:
      cost1=dQoS(i,csl[i],csl[i]+1)/dCR(i,csl[i],csl[i]+1)
      cost2=dQoS(i,csl[i],x)/dCR(i,csl[i],x)
      if cost1>cost2:
        cost.append([cost1,i])
      else:
        cost.append([cost2,i])
    cost.sort(key=lambda row: (row[0]), reverse=True)

#upgrade cost functions
def Upgrade_Cost():
  if csl[cost[0][1]]<(len(wt[cost[0][1]])-1):
    cost1=dQoS(cost[0][1],csl[cost[0][1]],csl[cost[0][1]]+1)/dCR(cost[0][1],csl[cost[0][1]],csl[cost[0][1]]+1)
    cost2=dQoS(cost[0][1],csl[cost[0][1]],len(wt[cost[0][1]])-1)/dCR(cost[0][1],csl[cost[0][1]],len(wt[cost[0][1]])-1)
    if cost1>cost2:
      cost[0][0]=cost1
    else:
      cost[0][0]=cost2
  else:
    cost.pop(0)

#alola algo
def ALOLA():
  global M
  global B
  while len(cost)>0:
    i=cost[0][1]
    p=wt[i][csl[i]+1]-wt[i][csl[i]]
    b=wm[i][csl[i]+1]-wm[i][csl[i]]

    if csl[i]<(len(wt[i])-1):
      if (p<=M) and (b<=B):
        csl[i]+=1
        M=M-p
        B=B-b
        Upgrade_Cost()
      else:
        cost.pop(0)
    else:
      cost.pop(0)

#driver code
ComputeCost()
ALOLA()
for i in range(n):
  print(csl[i])








    



