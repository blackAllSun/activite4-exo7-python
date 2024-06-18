t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']


t3=[]

for n in range(len(t1)):
    t3.append(t2[n])
    t3.append(t1[n])

print(t2)
