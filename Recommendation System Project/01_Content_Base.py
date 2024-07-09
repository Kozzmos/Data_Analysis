import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

movies_df = pd.read_csv("data/movies.csv")
ratings_df = pd.read_csv("data/ratings.csv")

# region Task1
# Movies içindeki title sütununda yıl bilgilerini parantezleriyler birlikte söküp atalım
# Year sütünü açarak parantezsiz şekilde yeni sütuna yazalım
# regex kullan
# Step 1: Title'da ki yılı ayır
movies_df["year"] = movies_df.title.str.extract(r'(\W{1}\d{4}\W{1})', expand=False)
# Step 2 yıldaki parantezden kurtul
movies_df["year"] = movies_df.year.str.extract(r'(\d{4})', expand=False)
# Step 3: title sütünundaki yıl bilgisini kaldır
movies_df["title"] = movies_df.title.replace(to_replace='(\W{1}\d{4}\W{1})', regex=True, value=" ")
# Step 4: title sütununda oluşturduğumuz boşluğu sil
movies_df["title"] = movies_df.title.apply(lambda x: x.strip())
# endregion

# region Task 2 VE TASK 3
# Genre Listesi oluştur

movies_genres_list = []

# ALTTAKİ HALİDE AYNI İŞİ GÖRÜYOR VE ÇALIŞIYOR  (HARDCODE)

# movies_df["genres"] = movies_df.genres.apply(lambda genres:genres.split(sep="|"))
# for eachlist in movies_df["genres"]:
#     for each in eachlist:
#         if each in movies_genres_list:
#             pass
#         else:
#             movies_genres_list.append(each)
# print(movies_genres_list)


#   YADA REGEX İLE SOYLE BİR KOLAYLIK YAPABILIRIZ
movies_genres_df = movies_df.copy()  #İLERİDE LAZIM OLUR DİYE AÇTIK REGEXLE BAĞLANTILI DEĞİL
for index, column in movies_df.iterrows():
    for i in column["genres"].split("|"):
        movies_genres_list.append(i)

unique_genres = np.unique(movies_genres_list)
unique_genres = np.delete(unique_genres, [0])
# endregion

# region Task4

# Yukarda elde edilen listenin her itemi için yani genre için movies_genres_df içerisine bir sütun açıp nan basın.

movies_genres_df = movies_genres_df.assign(**{col: np.nan for col in unique_genres})
# print(movies_genres_df.head().to_string())

# endregion

# region Task 5
# yapılan yeni sütunlara filmin kategorisine göre var yada yok şeklinde 1 yada 0 bas
for index, column in movies_df.iterrows():
    for genre in column["genres"].split('|'):
        movies_genres_df.loc[index, genre] = 1

movies_genres_df.fillna(0, inplace=True)
# print(movies_genres_df.head().to_string())
# endregion

# region Task 6
# Task6
user_input_df = pd.DataFrame([
    {"title": "Toy Story", "rating": 4},
    {"title": "Jumanji", "rating": 5},
    {"title": "Father of the Bride Part II", "rating": 5},
    {"title": "Heat", "rating": 1},
    {"title": "Space Jam", "rating": 5},
])
# Bu bir yeni kullanıcı datasıdır, ama id ler ve veriler eksiktir, bu df ye bizim dataframe deki id leri ve

merged_df = user_input_df.merge(right=movies_df[["title", "movieId"]], how="inner")
merged_df.drop([3, 5], axis=0, inplace=True) #heat filminden aynı isimde 3 filim olduğu için diğerlerinden kurtulalım
# print(merged_df.to_string())
# endregion

# region Task 7
# Task7
# userin rate ettiği filmleri id'lerini yukarıda saptadık, şimdi bu filmlerin sahip olduğu türlerin veri setini oluşturalım
user_favorite_genres = merged_df.merge(movies_genres_df, on="movieId")
user_favorite_genres.drop(["title_y", "year", "title_x", "rating", "movieId", "genres"], axis=1, inplace=True)
# print(user_favorite_genres.to_string())
# endregion

# region Task 8
# Task 8 user profile df oluştur series olarak
user_profile = user_favorite_genres.transpose().dot(user_input_df["rating"])
# print(user_profile)
# endregion

# region Task 9
# Task 9
# Movie matrix oluşturalım
movie_matrix = movies_genres_df.drop(labels=["title", "genres", "year"], axis=1)
movie_matrix.set_index("movieId", inplace=True)
# endregion

recommendation_matrix = pd.DataFrame(
    (movie_matrix * user_profile).sum(axis=1) / user_profile.sum()
)
recommendation_matrix.columns = ["Weighted Average"]
result_df = movies_df.merge(recommendation_matrix, on="movieId")
result_df.sort_values(by=("Weighted Average"), ascending=False, inplace=True)
print(result_df.head().to_string())

result_df.head(20).plot(
    x="title",
    y="Weighted Average",
    kind="bar"
)
plt.show()




