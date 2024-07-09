import pandas as pd

df = pd.read_csv('data/imdb.csv')
# print(df.to_string())
# Movie Title sütünun ilk 20 sini yazdır
# 1. Yol
# print(df[['Movie_Title']].head(20).to_string())
# # 2. Yol
# print(df[["Movie_Title"]][0:20])
# # 3. Yol
# print(df.loc[:20, "Movie_Title"])


# filtre => Rating  7.0 de olan
# Selec => Movie Ttile Raring ve YEAR release yazdfır
# print(df[["Movie_Title", "Rating", "YR_Released"]][df["Rating"] >= 7.0][20:50].sort_values("Rating", ascending=False))

# YRReleased bilgisi 2014 ve 2018 arası olan filmlerin title rating ve yr bilgisi listelee
# print(df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2018)][["Movie_Title", "Rating", "YR_Released"]])
# print(df[df["YR_Released"].between(2014, 2018)][["Movie_Title", "Rating", "YR_Released"]])

# Num reveiw 100k üstü yada rating 8, 9 arasında olan filmlerin title rating yr erelaeasede bilgilerini sıralra
print(
    df[
        (df["Num_Reviews"] >= 100000) | (df["Rating"].between(8, 9))
    ]
    [["Movie_Title", "Rating", "YR_Released"]].sort_values("Rating", ascending=False).to_string()
)




