import sys
from sklearn import svm
###Read Datafile

filename=sys.argv[1]
f1=open(filename,"r")
data=[]
l=f1.readline()
while (l != ""):
	a=l.split()
	l2 =[]
	for j in range (0,len(a),1):
		l2.append(float(a[j]))
	data.append(l2)
	l=f1.readline()

rows=len(data)
cols=len(data[0])
f1.close()

#Read labels from file
filename = sys.argv[2]
f2=open(filename,"r")
labels={}
n=[0,0]
l2=f2.readline()
while (l2 != ''):
	b=l2.split()
	labels[int(b[1])] = int(b[0])
	l2=f2.readline()
	n[int(b[0])]+=1

f2.close()
c=float(sys.argv[3])

X=[]
y=[]

for i in range (0,rows,1):	
		if(labels.get(i) != None):
			X.append(data[i])
			y.append(labels.get(i))
#print("X: ",X)
#y=[1 if x else 0 for x in y]
#print("y : ",y)

#clf=svm.SVC()
clf=svm.SVC(C=1,kernel="linear",probability=True,degree=1)
s=clf.fit(X,y)
#print("S : ",s)
for i in range(0,rows,1):
#	print("Label ",labels.get(i))
	if (labels.get(i) == None):
		t=[]
		t.append(data[i])
#		print("T=",t)
		x=clf.predict(t)
		print(x[0],i)
