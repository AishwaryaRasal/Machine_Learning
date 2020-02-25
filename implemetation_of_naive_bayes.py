import sys
filename=sys.argv[1]
f1=open(filename,"r")
i=0
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
l2=f2.readline()
while (l2 != ''):
	b=l2.split()
	labels[int(b[1])] = int(b[0])
	l2=f2.readline()


f2.close()
m0=[]
m1=[]
for i in range (0,cols,1):	
	m0.append(0)
	m1.append(0)

n0=0.0000001
n1=0.0000001
#summing up the row data and storing in mO and m1 classes
for i in range(0,rows,1):
	if (labels.get(i) != None and labels.get(i) == 0):
		n0+=1
		for j in range (0,cols,1):
			m0[j] += data[i][j]
	if (labels.get(i) != None and labels.get(i) == 1):
		n1+=1
		for j in range (0,cols,1):
			m1[j] += data[i][j]
for j in range (0,cols,1):
	m0[j] /= n0
	m1[j] /= n1
dist0=0
dist1=0
#print ("Means are: ")
#print (m0)
#print (m1)

var0=[]
var1=[]
for i in range (0,cols,1):
	var0.append(0.00000001)
	var1.append(0.00000001)

#summing up the row data and storing in mO and m1 classes
for i in range(0,rows,1):
	if (labels.get(i) != None and labels.get(i) == 0):
		for j in range (0,cols,1):
			var0[j] += ((m0[j] - data[i][j])**2)
	if (labels.get(i) != None and labels.get(i) == 1):
		for j in range (0,cols,1):
			var1[j] += ((m1[j] - data[i][j])**2)

for j in range (0,cols,1):
	var0[j] /= n0
	var1[j] /= n1
#print("Variances are: ")
#print(var0)
#print(var1)

for i in range (0,rows,1):
	w0=0
	w1=0	
	if (labels.get(i) == None):
		for j in range (0,cols,1):
			w0 += ((m0[j] - data[i][j])**2)/var0[j]
			w1 += ((m1[j] - data[i][j])**2)/var1[j]		
		if (w0 > w1):	
			print("1",i)
		else:
			print("0",i)
