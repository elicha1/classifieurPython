# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:30:15 2018

@author: aicha
"""
import numpy as np 
import matplotlib.pyplot as plt
from pylab import *
import math

        
def mean(numbers):
	return sum(numbers)/12
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/11
	return math.sqrt(variance)
def plusprobable(classs):
    
        maxix=max(classs)
        print(maxix)
        return maxix
def probamax(liste1,liste2):
    i=0

    prob1=calculateProbability(liste1)
    prob2=calculateProbability(liste2)
    for i in liste1:
        probx=max(prob1[i],prob2[i])
        print("probmax",probx)
def calculateProbability(classs):
    i=0
    zut=0
    probat=[]
    listedevaluers=[]
    classifieur=[[]]
    for g in classs:
        zut = zut+g  
    print("la somme des poits",zut)
    for g in classs:
        print("probat d'etre membre de claas ",i)
        x=((g)*(1/zut))
        print((g)*(1/zut))
        i=i+1
        probat.append(x)
        listedevaluers.append(i)
        classifieur.append([i,(g)*(1/zut)])
    print("le plus probable est:",plusprobable(probat),)
    print("le classifieur a :",classifieur)
    print("la probat a :",probat)
    return probat
def calculateiteratifnumbers(numbers,classification1):
    un=numbers.count(1)
    deux=numbers.count(2)
    trois=numbers.count(3)
    quatre=numbers.count(4)
    zero=numbers.count(0)
    print("zero se repete:")
    print(zero)
    classification1.append(zero)
    print("un se repete:")
    print(un)
    classification1.append(un)
    print("deux se repete:")
    print(deux)
    classification1.append(deux)
    print("trois se repete:")
    print(trois)
    classification1.append(trois)
    print("quatre se repete:")
    print(quatre)
    classification1.append(quatre)
    print("classification:")
    print(classification1)

listex=[]
listey=[]
classification1=[]
classx=[]
classy=[]
for x in "nananaanana": 
       tab1=np.random.randint(1,high=5,size=2,dtype='i')       
       print (tab1)
       plt.scatter(tab1[0], tab1[1], c = 'red')
       listex.append(tab1[0])
       listey.append(tab1[1])
       
plt.ylabel('fonction random')
plt.xlabel("l'axe des abcisses")
plt.show()
print(listex)
print ("la moyenne des x ")
print(mean(listex))
print ("la variance des x ")
print(stdev(listex))
print(listey)
print ("la moyennedes y ")
print(mean(listey))
print ("la variance des y ")
print(stdev(listey))
"""traitment des donnée combient dentier qui se repete """

print("expression guassienne sur x :") 
print(mean(listex)/stdev(listex))
print("expression guassienne sur y :") 
print(mean(listey)/stdev(listey))
plt.scatter(listex, listey, c = 'green')
plt.scatter([mean(listex)/stdev(listex)], [mean(listey)/stdev(listey)], c = 'yellow')
plt.show()
print("Dans x:")
calculateiteratifnumbers(listex,classx)
print("Dans y:")
calculateiteratifnumbers(listey,classy)
listeprobat1=calculateProbability(classx)
listeprobat2=calculateProbability(classy)
axedesx=[]
probatfinal=[]
classifieurT=[[]]
frontiereliste=[]
couteur=0
for i in {0,1,2,3,4}:
      listeprobatmax=max(listeprobat1[i],listeprobat2[i])
      probatfinal.append(listeprobatmax)
      classifieurT.append([i,listeprobatmax])
      axedesx.append(i)
      couteur=couteur+listeprobatmax*i
      frontiereliste.append(couteur)

print("holala",probatfinal)
print("le classifieur final",classifieurT)
plt.plot(axedesx,frontiereliste)
plt.show
plt.scatter( axedesx, probatfinal, c = 'gray')
plt.scatter(listex, listey, c = 'green')
plt.show()


"plt.scatter(axedesx, probatfinal, color = 'red', linestyle = 'solid')"
"plt.scatter(listex, listey, c = 'green')"
"plt.scatter([mean(listex)/stdev(listex)], [mean(listey)/stdev(listey)], c = 'yellow')"
input("appuez sur une touche pour finir")


   