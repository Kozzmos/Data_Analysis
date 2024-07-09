import pandas as pd

df = pd.read_csv("data/nba.csv")

# print(df["Salary"].max()) DENEMEM
# print(
#     df[
#         df["Salary"] == df["Salary"].max()
#     ]
#     [["Name","Salary"]]
# )
# takımlara göre maaş ort
# res = df.groupby("Team")["Salary"].mean()
# print(res)
# kaç farklı takım var
# res = df["Team"].nunique()
# print(res)
# Yaşı 20 ile 35 arasında olan oyuncvuların adı takımı yaşı yazdır yaşa göre azalan şekilde sıarala
res = (df[
           (df["Age"].between(20, 35))
       ]
       [['Name', 'Age', 'Team']].sort_values(by="Age", ascending=False)
       )
print(res)


# İsmi içinde and ifadesi geçen oyuncuları listeleyen custom func yaz

def hawlifunc(name: str):
    if "and" in name.lower():
        return True
    else:
        return False

print(
    df[
        df["Name"].apply(hawlifunc)
    ]
)

df.query()