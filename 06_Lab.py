import pandas as pd

# Merge & Join
# İki veri setinde oratak olarak byulunan sütunlardan faydalanıraka bu iki ver,i setinin birleştirilme isşlemrlerini yaptığımız fonksyonalar merge ve joindir SQL de de bulunur

customer = {
    "Customer_Id": [1, 2, 3],
    "First Name": ["Burak", "Hakan", "İpek"],
    "User Name": ["beast", "bear", "keko"]
}

orders = {
    "Order_Id": [1001, 1002, 1003, 1004, 1005],
    "Customer_Id": [1, 2, 3, 4, 5],
    "Order Date": ['2024.04.14', '2024.03.12', '2024.01.10', '2024.04.14', '2024.02.24']
}

df_customer = pd.DataFrame(customer)
df_orders = pd.DataFrame(orders)
#
# # Inner merge
#
# # print(df_customer.merge(right=df_orders,how="inner"))
#
# # Right merge
#
# print(df_customer.merge(how="right",right=df_orders, on="Customer_Id"))
# print(df_orders.merge(how="right",right=df_customer, on="Customer_Id"))

# Inner Join

print(df_orders.join(df_customer, how="inner", rsuffix="r_new"))
