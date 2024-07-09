import pandas as pd
import numpy as np

# number = [20, 30, 40, 50]
# letters = ["a","b","c","d"]
# scaler = 5
# dictionary = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }
#
# ny_array = np.array([20,30,40,40])
#
# # pandas kütüphanesinde 2 ana veri tipi bulunmkata. Bunlar Series ve DataFrame dir
# pd_series = pd.Series(number)
# print(pd_series)
# print(type(pd_series))
#
# # Pandas serisini Machine Learning algoritmalarındaki matematiksel işlemler yada istatiskiktsel methodaları için kullanacağız
# pd_series = pd.Series(letters)
# print(pd_series)
# # pd serisinde dictionary tipinde keyler index elementler ise value lar olarak atanır
# pd_series = pd.Series(dictionary)
# print(pd_series)
# # Slicing yapabiliyoruz
# print(pd_series[:2])
#
# # pandas serilerinin sahip olduğu bazı builtin fonskiypjlar ve attributelar
# # not aynı funclar ve attributeşar dataframe içinmde kullanılabilir
#
# print(pd_series.shape) #Serinin kaç boyutlu olduğunu göçsterier
#
# print(pd_series.dtype) #serinin veri tipini gösterir
#
# print(pd_series.ndim) #Serinin kaç katmanlı olduğunu gösterir
#
# print(pd_series.describe()) #serinin hzılıca count, mean, std, min, max vb özet bilgi verir
#
# print(pd_series.head(1)) #serinin ilk indexten başlayarak atanan değerdeki indexe kadar olan indexi döner. default 5 tir
#
# print(pd_series.tail(1)) #head in tersi
#
# print(pd_series >= 20)
#
# print(pd_series % 2 == 0)
#
# # Aggreate func olarak bilnene sum(), min(), max(), count(), mean() gibi fonsklar kullanılabilir
#
# print(f'Bütün değerleri toplamı: {pd_series.sum()}')
#
# opel_2000 = pd.Series([20,30,40], ["astra","corsa","vectra"])
# opel_2001 = pd.Series([50,60,70], ["astra","corsa","vectra"])
#
# total = opel_2000 + opel_2001
#
# print(total)

# Data Frame
# Pandas yoğun olarak kullanılan bir deiğer yapıdır excel gibi düşünebilirsiniz yan, satır ve sütundan oluşur
df = pd.DataFrame(
    data= np.random.rand(3, 5),
    index= ["A", "B", "C"],
    columns= ["Column1", "Column2", "Column3", "Column4","Column5"]
)

print(df)
# VERİ SEÇME (select)
# Series biçimnde çekme tek sütun çeker
print(df["Column2"])
print(type(df["Column2"]))
# DataFrame Biçiminde çekme ve birden fazla sütun çağırma olanağı sağlar
print(df[["Column1"]])
print(type(df[["Column1"]]))

# loc[] index değerlerini vererek istediğnizi index değerinde tutulan kayda erişebilirz.
print(df.loc["B"])
print(type(df.loc["B"]))

print(df.loc["C", "Column1"])
print(type(df.loc["C", "Column1"]))