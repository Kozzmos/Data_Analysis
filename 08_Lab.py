

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


# region Task 1
# xlsx formatındaki excel'in 'Canada by Citizenship' isimli sheet'i okuyoruz.
# ilk 20 satır ve son 2 satır okunmayacak.
df_can = pd.read_excel(
    'data/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),  # lambda x: x in x[0:20],
    skipfooter=2
)
# print(df_can.head(10).to_string())
# endregion

# region Task 2
# OdName => Country
# AreaName => Continet
# RegName => Region
# Eski sütüun isimlerini yenileriyle değiştirin
df_can.rename(columns={
    'OdName': 'Country',
    'AreaName': 'Continent',
    'RegName': 'Region'
}, inplace=True)
# print(df_can.head(10).to_string())
# endregion

# region Task 3
# AREA, REG, Type, Coverage, DevName sütunlarını silin
df_can.drop(
    columns=['AREA', 'REG', 'Type', 'Coverage', 'DevName', 'DEV'],
    axis=1,
    inplace=True
)
# print(df_can.head(10).to_string())
# endregion

# region Task 4
# Soru 1: Sütun başlıklarının tiplerini ekrna basın
# for column in df_can.columns:
#     print(type(column))

# Soru 2: Sütun başlıklarının hepsinin tipini string yapın
# map() ==> bize yenilenebilir bir objedeki (list, tuple) her bir öğe için bir işlem execute eder. Aşağıda ki kulanımında yenilenebilir obje df_can'in sütun başlıkları listesidir. Bu listede ki her bir item'in tipini string tipine map ediyoruz.
df_can.columns = list(map(str, df_can.columns))
# for column in df_can.columns:
#     print(type(column))
# endregion

# region Task 5
# veri setinde'ki var olan index yerine Country sütunun index olarak ayarlayalım.
df_can.set_index(keys='Country', inplace=True)
# print(df_can.head(10).to_string())
# endregion

# region Task 6
# Yıl yıl göçmen sayılarını toplayarak total isimli yeni bir sütuna yazdırın
df_can['Total'] = df_can.sum(axis=1, numeric_only=True)
# print(df_can['Total'])
# endregion

# region Task 7
# Veri setinde ki yılları baz alarak kendimize bir yıl listesi hazırlayalım lakin liste içirisinde ki yıl bilgileri string olsun
years = list(map(str, range(1980, 2014)))
# print(years)
# endregion

# region Task 8
# En çok göç vermiş 5 ülkeyi bulun. df_top_five_country isimli df'e kayıt edin.
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top_five_country = df_can.head()
# print(df_top_five_country.to_string())
# endregion

# region Task 9
# Yukarıda oluşturulan df_top_five_country veri seti ile, year isimli ilstemizi kullanarak yılları satırlara ülkeleri sütunlara dönüştürerek bir df elde edin bu df'i df_top_five_country üzerine assigned edin..
print(df_top_five_country[years].to_string())
df_top_five_country = df_top_five_country[years].transpose()
# print(df_top_five_country.to_string)

# endregion

# region Task 10
# Yukarıda oluşturan df_top_five_country veri setinden faydanalarank alan grafiği oluşturalım plot() kulannın
# df_top_five_country.plot(kind="area", stacked=True, figsize=(10, 7), alpha=0.25)
#
# plt.title(label="Immigrent Trend of Top 5 Country", color="r")
# plt.ylabel(ylabel="Number of Immigrent", c="r")
# plt.xlabel(xlabel="Years", c="r")
# plt.show()
# endregion

# region Task 11
# task 11 histogram grafiğinde göster
# 2013 yılındaki göçmen hareketlilğini göster
# x düzlemindeki değerleri numpy histogram() ilşe bulun

# count, bin_edges = np.histogram(df_can["2013"])
# print(count)
# print(bin_edges)
#
# df_can['2013'].plot(
#     kind="hist", figsize=(10, 7), xticks=bin_edges, color="b"
# )
#
# plt.title(label="Immigrent Trend of Top 5 Country in 2013")
# plt.ylabel(ylabel="Number of Country", c="r")
# plt.xlabel(xlabel="Number of Immigrent")
# plt.grid()
# plt.show()
# endregion

# region Task 12
# task 12
# baltık ülkelerin verdiği göçmen sayısını histogram edin
# yıllar index ülkeler sütun
# Denmark Norway Sweden
# histogram() fonksişyıonuna bin = 10 verin
# plot() a trenk verin coral, darkblue, green


# df_baltik = df_can.loc[["Denmark", "Norway", "Sweden"], years].transpose()
# count, bin_edges = np.histogram(df_baltik)
#
# df_baltik.plot(
#     kind="hist", figsize=(10, 7), xticks=bin_edges, color=["coral", "darkblue", "green"], stacked=True
# )
#
# plt.title(label="Immigrents of Baltik Countries")
# plt.ylabel(ylabel="Countries", c="r")
# plt.xlabel(xlabel="Number of Immigrent")
# plt.grid()
# plt.show()
# endregion

# region Task 13

# 1980-2013arası ıceland göçmenleri çubuk grafik

# df_iceland = df_can.loc["Iceland", years]
#
# df_iceland.plot(
#     kind="bar",
#     figsize=(10, 7)
# )
# plt.title(label="Immigrents of Iceland")
# plt.ylabel(ylabel="Immigrents")
# plt.xlabel(xlabel="Years")
# plt.show()
# endregion

# task 14 kıtalara göre göçmen bilgisi pasta garfiğiğ

df_pasta = df_can.groupby(by="Continent").sum(numeric_only=True)

df_pasta["Total"].plot(
    kind="pie",
    figsize=(10, 7),
    startangle=90,
    autopct="%1.1f%%", #Her dilime gelicek göçmen miktarını formatlıyarak yazdırıyop
    labels=None, #ülkelerin pasta diliminde gözükmesini engelledik
    shadow=True,
    pctdistance=1.1, #yüzde etiketinin her dilimden olan uzaklığını yazdık
    explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
)

plt.title(label="Immigrents of Iceland")
plt.axis("equal")  #pasta grafiğinin dairsel olmasını sağlayarak grafiğin en boy oranını kendi eşitliyo
plt.legend(
    labels=df_pasta.index,
    prop={
        'size': 8
    }
)
plt.show()


