import numpy 

x1,y1 = 2 , 0.7
x2,y2 =  4 , 0.5
#olusturacagimiz dizilere atayacagimiz degerleri tutan counterlar
counter_1 = 0
counter_2 = 0
#histogramlardaki sifirdan farkli ilk degeri tutacak index params
counter_index_1=0
counter_index_2=0
flag1=0
flag2=0
#indexler arasi guncellenecek olan distance degeri
d=0
#En son histogramlar arasi bulacagimiz buyuk distance
D=0
#rastgele deger atayarak olusturulan onbin elemanli diziler
l1 = numpy.random.normal(x1,y1,10000)
l2 = numpy.random.normal(x2,y2,10000)
#elemanlarinin her biri sifir olan 40 elemanli diziler
array_1 = numpy.zeros(40)
array_2 = numpy.zeros(40)

#40 elemanli dizilere deger atamalari
for i in range (0,19):
    
    for j in range (0,9999):
        if i == round(l1[j]):
            counter_1+=1
        if i == round(l2[j]):
            counter_2+=1
    array_1[i+20] += float(counter_1)/10000
    array_2[i+20] += float(counter_2)/10000
    counter_1 = 0
    counter_2 = 0

print(array_1)
print(array_2)
""" asagidaki iki for ile histogramlardaki 0 dan farkli ilk degerlerin
indexlerini aliyoruz"""
for i in range(0,39):
    if flag1==0:
         if array_1[i]!=0:
            counter_index_1=i
            flag1=1           
for i in range(0,39):
    if flag2==0:
         if array_2[i]!=0:
            counter_index_2=i
            flag2=1
"""Wasserstein metric yontemiyle histogramlar arasi mesafeyi 
hesapliyoruz"""

#ilk isleme girecek degerlerin distance degerini hesaplamasi
d=abs(abs(counter_index_1)-abs(counter_index_2))

#sonrasinda gelen degerlerin hesaplanmasi
#while counter_index_1 < 39 | counter_index_2 < 39 :
for i in range (0,20):
    print(counter_index_1)  
    print(counter_index_2) 
    print(D)    
    if array_1[counter_index_1] < array_2[counter_index_2]:
            D=d*array_1[counter_index_1]
            array_2[counter_index_2]=array_2[counter_index_2]-array_1[counter_index_1]
            array_1[counter_index_1]=0
            counter_index_1+=1
            
    if array_1[counter_index_1]==array_2[counter_index_2]:
            D=d*array_1[counter_index_1]
            array_1[counter_index_1]=0
            array_2[counter_index_2]=0
            counter_index_1+=1
            counter_index_2+=1
    if array_1[counter_index_1] > array_2[counter_index_2]:
            D=d*array_1[counter_index_1]
            array_1[counter_index_1]=array_1[counter_index_1]-array_2[counter_index_2]
            array_2[counter_index_2]=0
            counter_index_2+=1
            
print(counter_index_1)
print(counter_index_2)   
            
                

print(array_1)
print(array_2)
      
print(sum(array_1))
print(sum(array_2))        
 
print(D)
print(d)