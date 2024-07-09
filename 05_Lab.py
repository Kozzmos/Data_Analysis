import pandas as pd

df = pd.read_csv("data\youtube-ing.csv")


# en çok görüntüleme sahiop ilk 10 farklı video title ve view yazdır

# res = (
#     df.groupby(by="title")[["views"]]
#     .sum(numeric_only=True)
#     .sort_values(by="views", ascending=False)
#     .head(10)
# )
# print(res)

# categorilere göre like ort

# print(
#     df.groupby(by="category_id")[["likes"]]
#     .mean(numeric_only=True)
#     .sort_values(by="likes", ascending=False)
# )

# hangi kanal ne kadar yorum almış

# print(
#     df.groupby(by="channel_title")[["comment_count"]]
#     .sum(numeric_only=True)
#     .sort_values(by="comment_count", ascending=False)
#     .head(10)
# )

# her video için kullanılan tag sayısı için kullanılan tag sayuısını tag count isimli yeni bir sütün yaratalım
# title ve tag count ekrana bas

# def tag_counter(tags: str):
#     counter = len(tags.split(sep="|"))
#     return counter
# df["tag_count"] = df["tags"].apply(tag_counter)
# print(df[["title", "tag_count"]].sort_values(by="tag_count"))

# lambda version

# tag_counter_lambda = lambda tags:len(tags.split(sep="|"))
# df["tag_count"] = df["tags"].apply(tag_counter_lambda)
# print(df[["title", "tag_count"]].sort_values(by="tag_count", ascending=False))

# Her bir videonun like dislike oranını bulun
# like avg sütununa yazın

# def like_dislike_avg(data_set: pd.DataFrame):
#     data_set.reset_index()
#     percent = data_set["likes"] / (data_set["likes"] + data_set["dislikes"]) * 100
#     percent.fillna(0, inplace=True)
#     return percent.tolist()
#
# # print(df.shape)
# # lst = like_dislike_avg(df)
# # print(lst)
# # print("listenin len",count(lst))
# df["like_avg"] = like_dislike_avg(df)
# print(df[["title", "like_avg"]].sort_values(by="like_avg", ascending=False).head(10))

def like_dislike_avg(data_set: pd.DataFrame):
    percent = df["likes"] / (df["likes"] + df["dislikes"]) * 100
    percent.fillna(0, inplace=True)  # Fill NaN values with 0
    return percent.tolist()

df["like_avg"] = like_dislike_avg(df)

print(df[["title", "like_avg"]].sort_values(by="like_avg", ascending=False).head(10))

# OR Second Way

# def like_dislike_avg_2(data_set: pd.DataFrame):
#     like_list = list(data_set["likes"])
#     dislike_list = list(data_set["dislikes"])
#
#     comb_list = list(zip(like_list, dislike_list))
#     avg_list = []
#     for like, dislike in comb_list:
#         if like + dislike == 0:
#             avg_list.append(0)
#         else:
#             avg_list.append(like/(like+dislike))
#     return avg_list
#
# df["like_avg"] = like_dislike_avg_2(df)
# print(df[["title", "like_avg"]].sort_values(by="like_avg", ascending=False).head(10))
