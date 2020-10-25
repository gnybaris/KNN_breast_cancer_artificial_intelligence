# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:04:18 2020

@author: PC 

@gnybaris

https://github.com/gnybaris/KNN_breast_cancer_artificial_intelligence

"""
import numpy as np
import pandas as pd
#from sklearn.preprocessing import Imputer
#from sklearn.impute import SimpleImputer
#Imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#from sklearn import cross_validation
from sklearn.model_selection import cross_val_score
#from sklearn import train_test_split
from sklearn.model_selection import train_test_split

kanser_verileri = pd.read_csv("C:\\Users\\PC\\Desktop\\Gögüs_Kanseri_Testi\\breast-cancer-wisconsin.data.txt")

kanser_verileri.drop(['id'], axis=1)

y = kanser_verileri.benormal
x = kanser_verileri.drop(['benormal'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

tahminler = KNeighborsClassifier()
tahminler.fit(X_train, y_train)


# Test edilmesini isteğimiz hastanın değerlerini girerken id kısmına "0" yazıyoruz.

#hasta=np.array(input()).reshape(1,-1)

print("Gireceğiniz ilk değer id olacağı için id numaranızı 0 olarak giriniz...")
hasta = []
for i in range(0, 10): 
    girdi = int(input("Id ile birlikte 10 haneli hasta sonuçlarını girin : "))
    hasta.append(girdi) # adding the element 

print(hasta)

basariOranı=tahminler.score(X_test, y_test)
yüzdeoran = basariOranı*100
yüzdeoran = round(yüzdeoran,2)


print("Yüzde", yüzdeoran," oranında benormal sonucu: ")

hasta = np.array(hasta).reshape(1,-1)

#hasta = np.array([0,1,7,1,0,3,6,1,9,2]).reshape(1,-1)

type(tahminler.predict(hasta))

print(tahminler.predict(hasta))

#https://github.com/gnybaris/KNN_breast_cancer_artificial_intelligence


#https://github.com/gnybaris











"""
for z in range(25):
    z = 2*z+1
    print("En yakın",z,"komşu kullandığımızda tutarlılık oranımız")
    tahmin = KNeighborsClassifier(n_neighbors=z, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='euclidean', metric_params=None, n_jobs=1)
    tahmin.fit(x,y)
    ytahmin = tahmin.predict(x)

    basari = accuracy_score(y, ytahmin, normalize=True, sample_weight=None)
    print(basari)
"""    
"""
tahmin = KNeighborsClassifier(n_neighbors=3, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='euclidean', metric_params=None, n_jobs=1)
tahmin.fit(x,y)
ytahmin = tahmin.predict(x)

basari = accuracy_score(y, ytahmin, normalize=True, sample_weight=None)
print("Yüzde",basari*100," oranında:" )

print(tahmin.predict([1,2,2,2,3,2,1,2,3,2]))
"""