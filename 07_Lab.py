

import pandas as pd
import numpy as np


df = pd.read_csv('data/auto.csv')


# Veri setimizde sütun isimleri yok. Veri setimize sütun isimleri basalım
df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Hatalı ve Eksik Değerleri Saptama
# Veri setimizde bazı hücrelerde '?' sembolü bulunmaktadır. Şayet veri setmizde bu tarz anormalliklerin bulunmaıs durumunda veri setimizi her hangi bir ML algoritmasına sokup çalıştıramayız. Çünkü ML algoritmaları matamatiksel işlemlere dayanmaktadır. Örneğin Regrasyon, Entropi vb. Bu sebepten ötürü veri setimizde ki eksik yada hatalı alanları saptayıp onları ele almamız ML algoritması için hazırlamamız gerekmektedir.


# Step I
# Eksik ve hatalı verileri ML algortimasında kullanamıyoruz. Bunu için numpy kütüphanesinde bulunan NaN yani diğer programlama dillerinde Null diye geçen boş anlamına gelen veriyi eksik ve hatalı verilerle değiştireceğiz böylelikle ML algoritmasında bir hata ile karşılaşmayacağız.
df.replace(to_replace='?',
           value=np.nan,
           inplace=True)
# print(df.head().to_string())

# Step II - Count Missing Values
# Ne kadar eksik değerim var saptayalım
# isnull() fonksiyonu 'NaN' gördüğü hücrelere 'True' görmediği yerlere 'False' değeri basar. Sonuç olarak bize True ve False değerlerine sahip bir df döner
# missing_value_df = df.isnull()
# print(missing_value_df.head().to_string())

# aşağıdaki söz diziminde ilgili veri setinde ki başlıkların listesini verir.
# missing_value_df.columns.values.tolist()

# for item in missing_value_df.columns.values.tolist():
#     print(f'Column Name: {item}\n{missing_value_df[item].value_counts()}')

# Step III - Handling Missing Values
# Yukarıda hangi sütunda ne kadar missing value'muz var detect ettik şimdi onları handle edelim.
# Peki neden uğraşıyoruz. Silip kurtulamaz mıyız? ML algoritmalarında ne kadar farklı veri ile algortimamızı train edersek o kadar başarılı sonuçlar elde ederiz bu nedenle her bir satır veri bizim için kıymetlidir.

# Eksik verileri ele alırken iki yöntem kullanabiliriz.
# Bunlar:
# 1. İlgili sütunda bulunan değerlerin ortalamasını alarak bu ortalama değeri eksik değerlerin bulunduğu hücreye yazabiliriz
# 2. Yine ilgili sütunda bulunan değerlerin frekans aralığını bulup eksik değerlerin bulunduğu hücrelere yazabiliriz. BUrada frekans aralığından kastımız ilgili sütunda bulunan değerlerin ne sıklıkla ilgili sütunda bulunduğudur.

# Ortalama Değeri Bularak Eksik Veriler İle Değiştirme
df['normalized-losses'] = df['normalized-losses'].replace(to_replace=np.nan,
                                                          value=df['normalized-losses'].astype(float).mean())
# print(df.head().to_string())


# Frekans Aralığı İle Eksik Verileri Değiştirme
# value_counts() ==> bir sütunda geçen farklı değerlerin kaç tane olduğunu bize söyler
# idxmax() ==> ilgili sütunda en çok geçen değeri bize söyler
df['num-of-doors'] = df['num-of-doors'].replace(to_replace=np.nan,
                                                value=df['num-of-doors'].value_counts().idxmax())


# Veri Standardizasyonu
# ML algoritmalarında kullanılacak veri setinde ki değerlerin belirli bir standartda olması gerekmektedir. Örneğin 2 veri kaynağımız olsun birisi amerikadan diğeri avrupadan. Avrupadan gelen verilerde ki yakıt türü kilometre başına litredir lakin amerika da mile per galeon olarak hesaplanmaktadır. Yada avrupada kilogram kullanılırken amerika da pound yada libre birimleri kullanılmaktadır. Veri setinde ki bu farklı birimlere sahip değerler ML algortimamızın train edilip ürettiği sonuçları olumsuz yönde etkileyecektir. Bu yüzden verimizin bir standartta olması gerekmektedir.
df['city_l/km'] = 235/df['city-mpg']
df['highway_l/km'] = 235/df['highway-mpg']


# Veri Normalizasyonu
# Belirli bir sütunda ki değerlerin benzer bir aralığa kavuşması işlemine veri normalizasyonu diyoruz. Veri setimizde bulunna lenght, width gibi değerlerin 0.1 - 1.9 vb bir aralığa yani daha küçük scalar büyüklüklere dönüştürülmesi için yapılan bir işlemdir.
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()

print(df[['length', 'width', 'height']])


# Dummy Variable
# Veri setimizde sözel yada categorical değerler olabilir. BU değerleir ML algoritmalarında kullanabilmek için onları scaler büyüklüklere dönüştürmemiz gerekmektedir.
# Veri setimizde 'fuel-type' sütunumuzda categorical değerler diesel, gas vb bulunmaktadır. Bunları scaler büyüklüklere dönüştürelim
dummy_variable_df = pd.get_dummies(df['fuel-type'], dtype='float')
print(dummy_variable_df.head())


# bakımını yaptığımız veri setimizi yeni bir excel yazalım
df.to_csv('clean_auto.csv')
