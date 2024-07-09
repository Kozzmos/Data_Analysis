import pandas as pd

users = {
    "Employee": ["Burak","Bora","Akif","Cem","Barış"],
    "Occupation": ["Kumarbaz", "Kalpazan", "Kaçakçı", "Kalpazan", "Kumarbaz"],
    "Neighbor": ["Sarıyer", "Nişantaşı", "Suadiye", "Nişantaşı", "Suadiye"],
    "Income": [5000, 4000, 5000, 4000, 5000],
    "Age": [35, 28, 35, 28, 35]
}

# Group By
# Veri setindeki bazı değerlere göre verilerimizi gruplara ayırır. SQL temelli veri tabanlarılarında da aynı mantık vardır

df = pd.DataFrame(users)
# print(df.to_string())
# # mesleklere göre grupla
# print(df.groupby("Occupation").groups)
# # hangi semtte kimler oturuyor
#
# for name, groups in df.groupby("Neighbor"):
#     print(name)
#     print(groups)

# hangi semtte kaç çalışan var
print(df.groupby("Neighbor")["Employee"].count())

# mesleklere göre toplam maaş

res = df.groupby("Occupation")["Income"].sum()
print(res)

# mesleklere göre yaş ortalaması
res = df.groupby("Occupation")["Age"].mean()
print(res)