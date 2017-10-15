import pylab as plt
mySanples =[]
myLinear=[]
myQuandratic=[]
myCubic=[]
myExponential=[]

for i in range(0,30):
    mySanples.append(i)
    myLinear.append(i)
    myQuandratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.figure('lin and qua')# this windows for the plot below
plt.clf()#o clear the figure
plt.ylim(0,900)
plt.plot(mySanples,myLinear,'-b',label='linear',linewidth=2.0)
plt.plot(mySanples,myQuandratic,'ro ',label='Quadratic',linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')

plt.figure('lin and myQuandratic')# this windows for the plot below
plt.clf()#o clear the figure
plt.subplot(211)# 2 row 1 column and location 1
plt.xlabel('X')# are added below the figure. you can also recall the figure later and add label 
plt.ylabel('Y') 
plt.ylim(0,900)
plt.plot(mySanples,myLinear,'-b',label='linear',linewidth=2.0)
plt.ylim(0,900)
plt.subplot(212)# 2 row 1 column and location 2
plt.plot(mySanples,myQuandratic,'ro ',label='Quadratic',linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')



plt.figure('myCubic')
plt.clf()
plt.ylim(0,140000)
plt.subplot(121)# 1 row 2 column and location 1
plt.plot(mySanples,myCubic,'g^',label='Cubic',linewidth=4.0)
plt.ylim(0,140000)
plt.subplot(122)# 1 row 2 column and location 2
plt.plot(mySanples,myExponential,'r--',label='Exponential',linewidth=4.0)
plt.legend()
plt.title('Cubic vs. Exponential')


plt.show()
print(len(mySanples),len(myLinear))
print("Plotting")
