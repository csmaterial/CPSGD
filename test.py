from sys import argv
import numpy as np
from os.path import exists

# script, input_file, out_file = argv
script, input_file = argv
#246397
row = 2

#str->list	
def get_list(f):
	temp = f.readline()
	x = temp.split('\t')
#	print "get line"
	return x
#list->get x[i]
def get_num(i,x):
	a = x[i]
	b = int(a)
	return b
	

file = open(input_file)
a= []
b= []
c= []
d= []
e= []
Uu =0
Ii =0

step = 200 
r = 50 # 
alpha = 0.01
beta = 0.1

# get data
for j in range(row): 
	x = get_list(file)
#	print "this %d list is"%j,x
	tem = get_num(0,x)
	a.append(tem)
	if	Uu < tem :
		Uu = tem
	tem = get_num(1,x)
	b.append(tem)
	if	Ii < tem :
		Ii = tem
	tem = get_num(2,x)
	c.append(tem)
	tem = get_num(3,x)
	d.append(tem)	
	tem = get_num(4,x)
	e.append(tem)

#create 3-tensor
M = np.zeros((Uu,Ii,3),dtype=np.int16)	
print "create the matrix"
for i in range(row):
		Ut = a[i]-1
		It = b[i]-1

		M[Ut,It,0] = c[i]
		M[Ut,It,1] = d[i]
		M[Ut,It,2] = e[i]

# Matrix decomposition
U = np.random.random(Uu,50)
I = np.random.random(Ii,50)
A = np.random.random(Aa,50)

for i in range(step): #step
	for j1 in range(Uu): #1-U
		for j2 in range(Ii): #2-I
			for j3 in range(3):#3
				if M[j1,j2,j3] > 0:
					error = M[j1,j2,j3]
					for j4 in range(r):
						error = error - U[j1,j4]*I[j2,j4]*A[j3,j4]
					#???why not together
					for j5 in range(r):
						U[j1,j5] = U[j1,j5] - alpha*beta*U[j1,j5] - alpha*error*I[j2,j5]*A(j3,j5)
						I[j1,j5] = I[j1,j5] - alpha*beta*I[j1,j5] - alpha*error*U[j2,j5]*A(j3,j5)
						A[j1,j5] = A[j1,j5] - alpha*beta*A[j1,j5] - alpha*error*U[j2,j5]*I(j3,j5)


print U	
print I 
print A 					
'''test			
print M

print a
print b
print c
print d
print e
'''
print "Uu:",Uu
print "Ii:",Ii

'''output data
outfile = open(out_file,'w')

outfile.write(a)
outfile.write(b)
print "write over"
outfile.close()
file.close()
'''
