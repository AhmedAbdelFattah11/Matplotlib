import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[50,35,64,15,90,86,91]

plt.plot(x,y,color='Red',marker='D',linestyle='')

###################################################3


days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,55]
min_t=[40,41,42,43,45,46,44]
avg=[45,48,46,47,46,48,45]

plt.plot(days,max_t,label="max")
plt.plot(days,min_t,label="min")
plt.plot(days,avg,label="avg")

plt.xlabel('Days')
plt.ylabel('Temprature')
plt.title("wether")

plt.legend(loc='best')

#######################
import numpy as np
company=['as','ad','af','ag']
revenue=[90,136,89,27]
ypos=np.arange(len(company))
plt.xticks(ypos,company)
plt.bar(ypos,revenue)
########
A=[5,6,7,8,9,6,2,5]
B=[5,8,6,4,7,9,3,2]
plt.hist([A,B],bins=(2,4,6,8,10),color=['green','orange'])


##################pie

x=[1400,600,300,500,410]
y=['food','clean','rady','gabry','fattah']
plt.axis('equal')
plt.pie(x,labels=y,radius=1.5,autopct='%0.1f%%',explode=[0,0,.2,0,.1])

plt.savefig('pie.png')





































 