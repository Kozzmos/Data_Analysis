

import pandas as pd
from math import sqrt

movies_df = pd.read_csv('data/movies.csv')
ratings_df = pd.read_csv('data/ratings.csv')

movies_df['year'] = movies_df.title.str.extract(pat=r'(\W{1}\d{4}\W{1})', expand=False)
movies_df['year'] = movies_df.year.str.extract(pat=r'(\d{4})', expand=False)
movies_df['title'] = movies_df['title'].str.replace(pat=r'(\W{1}\d{4}\W{1})', repl=' ', regex=True)
movies_df['title'] = movies_df['title'].apply(lambda x: x.rstrip())

ratings_df.drop(['timestamp'], axis=1, inplace=True)

user_input_df = pd.DataFrame([
    {'title': 'Toy Story', 'rating': 4},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Father of the Bride Part II', 'rating': 5},
    {'title': 'Heat', 'rating': 5},
    {'title': 'Space Jam', 'rating': 5},
])

merged_df = pd.merge(user_input_df, movies_df, on='title')
merged_df.drop(index=[4, 5], axis=0, inplace=True)
merged_df.drop(labels=['year'], axis=1, inplace=True)
merged_df.reset_index(drop=True, inplace=True)
# print('merged df output:')
# print(merged_df.to_string())
# print('==============')


# yeni gelen kullanıcı ile hali hazırda yanı filmleri rate etmiş kullanıcıları saptayalım
user_subset_df = pd.merge(
    left=ratings_df,
    right=merged_df,
    left_on='movieId',
    right_on='movieId',
    how='inner'
)


user_subset_df.drop(
    labels=['title', 'rating_y'],
    axis=1,
    inplace=True
)
user_subset_df.rename(
    columns={
        'rating_x': 'rating'
    },
    inplace=True
)
# print(user_subset_df.head().to_string())

# artık user_subset_df içerisinde yeni gelen kullanıcı ile aynı filmleri rate ettmiş kullanıcılar var
# userId'lerine göre ilgili veri setini gruplayalım
user_subset_group = user_subset_df.groupby(by='userId')

# for name, group in user_subset_group:
#     print(f'Group Name: {name}\n'
#           f'Group: {group}')

# yukarıda elde ettiğimiz veri kelimesini sort edelim ki yeni gelen kullanıcını rate ettiği filmlerle aynı sırada aynı filmleri rate etmiş kullanıcıları saptayalım
sorted_user_subset_group = sorted(
    user_subset_group,
    key=lambda x: len(x[1]),
    reverse=True
)

# çalışmanın bu safhasında yeni gelen kullanıcı ile bu kullanıcın rate ettiği filmeleri hali hazırda rate etmiş kullanıcılar arasında ki korelasyonu bulacağız. Burada korelasyon ile kullanıcılar arasında ki ilişkiyi inceleyeceğiz aslında ilişkiyi ortaya koyacağız. Korelasyon istatistik biliminde yoğun olarak kullanılmaktadır ve farklı korelasyon türleri bulunmaktadır. Biz burada pearson korelasyonunu kullanacağız.

# korelasyon sonucunu store etmek için bir dictionary yaratalım
pearson_corellation_dict = {}

for userId, group in sorted_user_subset_group:
    # group girdisini ile user_input_df her iki taraftada bulunan movieId sütununa göre sıralıyoruz. böulelikle değerler daha sonra bir birine karışmayacak nizami bir sırlama elde edeceğiz.
    group.sort_values(by='movieId', inplace=True)
    merged_df.sort_values(by='movieId', inplace=True)

    # pearson korelasyonunu hesaplamak için kullanılan formülü burada teşekkül etmemiz gerekecek bu yüzden formülde bulunan N katsayısını tanımlıyoruz.
    n_rating = len(group)

    # merge işlemi yaparken merge etme şeklimizden bazı gereksiz sütunlar elde ediyoruz. alternatif bir yöntem ile merge işemi yapacağım.
    # group'lar içerisinde ki movieId ile user_input_df'teki movieId leri kullanarak veri setlerini birleştiriyporuz. unutmayın yukarıda iki veri setini aynı hizaya soktuk. ilk yaptığımız işlem oydu şimdi birleştiriyoruz. ediyoruz.
    temp_df = merged_df[merged_df['movieId'].isin(group['movieId'].tolist())]

    # pearson korelasyonunda ki argümanlarda kullanılmak üzere rating bilgilerini elde ediyorum
    temp_rating_list = temp_df['rating'].tolist()
    temp_group_list = group['rating'].tolist()

    # bu ana kadar korelasyon formülünü uygulamak için ihtiyaç duyulan argümanların hazırlığını yaptık şimdi X ve Y olarak nitelendireceğimiz iki attribute arasında ki benzerlliği bulacağız.

    Sxx = sum([i ** 2 for i in temp_rating_list]) - pow(sum(temp_rating_list), 2) / float(n_rating)
    Syy = sum([i ** 2 for i in temp_group_list]) - pow(sum(temp_group_list), 2) / float(n_rating)

    Sxy = sum(i * j for i, j in zip(temp_rating_list, temp_group_list)) - sum(temp_rating_list) * sum(temp_group_list) / float(n_rating)

    if Sxx != 0 and Syy != 0:
        pearson_corellation_dict[userId] = Sxy / sqrt(Sxx * Syy)
    else:
        pearson_corellation_dict[userId] = 0

pearson_df = pd.DataFrame.from_dict(pearson_corellation_dict, orient="index")
pearson_df.columns = ["similarity index"]
pearson_df["userId"] = pearson_df.index
pearson_df.reset_index(drop=True, inplace=True)
sorted_pearson_df = pearson_df.sort_values(by="similarity index", ascending=False)

top_user_rating_df = sorted_pearson_df.merge(
    ratings_df,
    on="userId",
    how="inner"
)

top_user_rating_df["weighted rating"] = top_user_rating_df["similarity index"] * top_user_rating_df["rating"]

temp_user_rating = top_user_rating_df.groupby("movieId").sum()[["similarity index", "weighted rating"]]

temp_user_rating["recommendation score"] = temp_user_rating["weighted rating"] / temp_user_rating["similarity index"]

temp_user_rating = temp_user_rating.sort_values(by="recommendation score", ascending=False)

recommendation_df = pd.merge(
    left=temp_user_rating,
    right=movies_df,
    on="movieId",
    how="inner"
)
sorted_recommendation = recommendation_df.sort_values(by="similarity index")
print(sorted_recommendation.head(100).to_string())

