import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
day_df= pd.read_csv("day_bikedata.csv")
st.title("Proyek Akhir 1: Bike Sharing Dataset Exploratory Analysis")
st.header('Deskripsi Statistik Data')
st.write("Menampilkan informasi count, mean, standard deviasi, quartile, nilai minimum dan maksimum dari variabel-variabel yang ada pada data")

selected_columns = st.multiselect('Pilih variabel:', day_df.columns)
if not selected_columns:
    st.warning('Silakan pilih setidaknya satu variabel.')
else:
    st.write(day_df[selected_columns].describe())

st.header('Rata-rata Pengguna Peminjaman Sepeda Berdasarkan Musim')
st.write ('Menampilkan rata-rata dari casual, registered, dan total users peminjam sepeda berdasarkan musim.')
selected_column = st.selectbox('Pilih kolom:', ['casual', 'registered', 'count'])
grouped_data = day_df.groupby('season')[selected_column].mean()
st.write(grouped_data)

st.header('Visualisasi dan Explanatory')
def main():
    st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Musim')
    st.write ('Total banyaknya peminjam sepeda paling tinggi yaitu pada saat musim gugur, kemudian dengan selisih yang tipis disusul oleh musim dingin. Total pada musim dingin dan musim panas juga memiliki perbedaan yang tipis, membuat musim panas berada diurutan ketiga. Terakhir, total peminjam sepeda paling rendah diantara keempat musim tersebut yaitu pada musim semi.')
    plt.figure(figsize=(8, 6))
    plt.bar(x=day_df['season'], height=day_df['cnt'], edgecolor='none') 
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman')
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Musim', fontsize = 20, fontweight='bold')
    st.pyplot(plt)
if __name__ == '__main__':
    main()

st.write('')
st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Musim Pada Masing-Masing Tahun')
st.write('Total peminjam sepeda pada tahun 2011 mengalami peningkatan yang signifikan di tahun 2012 pada setiap musim. Urutan dari tertinggi ke terendah total peminjam sepeda berdasarkan musim yaitu musim gugur, musim dingin, musim panas, dan terakhir musim semi. Urutan tersebut berlaku untuk tahun 2011 dan 2012.')
fig, ax = plt.subplots()
sns.barplot(data=day_df, x='season', y='cnt', hue='yr', palette=['orange', 'darkblue'], ax=ax, ci=None)
plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Jumlah Peminjaman Sepeda Berdasarkan Musim', fontweight='bold')
plt.legend(title='Year')
st.pyplot(fig)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df.set_index('dteday', inplace=True)
monthly_data = day_df.resample('M').sum()
def main():
    st.subheader('Line Chart Jumlah Peminjaman Sepeda Berdasarkan Bulan')
    st.write('Tahun 2011 dan 2012 memiliki pola yang sama, yaitu sama-sama membentuk kurva cembung. Meskipun terjadi peningkatan pada tahun 2012 namun pola grafiknya terlihat sama. Hal tersebut terjadi karena pembentukan kurva dipengaruhi oleh musim yang terjadi, dimana musim-musim tersebut akan berulang pada setiap tahunnya.')
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data.index.astype(str), monthly_data['cnt'])
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    plt.title('Line Chart Jumlah Peminjaman Sepeda Berdasarkan Bulan', fontsize = 20, fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
if __name__ == '__main__':
    main()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hubungan antara Humidity dengan Total Banyaknya Peminjam Sepeda")
    st.write('Hubungan antara humidity dan total peminjam sepeda merupakan hubungan yang negatif, artinya bahwa ketika humidty rendah maka total peminjam sepeda tinggi/meingkat. Namun karena grafik yang terbentuk kemiringannya rendah dan hampir mendekati horizontal maka dapat dikatakan bahwa humidity tidak secara signifikan mempengaruhi total peminjaman sepeda.')
    def main():
      sns.set(style="whitegrid")
      plt.figure(figsize=(10, 6))
      sns.regplot(x=day_df['hum'], y=day_df['cnt'],color='darkblue', scatter_kws={'s': 15})
      plt.xlabel('Humidity')
      plt.ylabel('Count')
      plt.title('Korelasi Humidity dengan Total Banyaknya Peminjam Sepeda', fontsize = 20, fontweight='bold')
      st.pyplot(plt)
    if __name__ == '__main__':
       main()
 
with col2:
    st.subheader("Hubungan antara Temperature dengan Total Banyaknya Peminjam Sepeda")
    st.write('Hubungan antara temperatur dan total peminjam sepeda merupakan hubungan yang positif, artinya bahwa ketika temperatur rendah maka total peminjam sepeda juga rendah dan berlaku sebaliknya. Grafik yang terbentuk memiliki kemiringan yang signifikan dan titik-titiknya menyebar mendekati garis tersebut maka dapat dikatakan bahwa temperatur secara signifikan mempengaruhi total peminjaman sepeda.')
    def main():
      sns.set(style="whitegrid")
      plt.figure(figsize=(10, 6))
      sns.regplot(x=day_df['temp'], y=day_df['cnt'], color='darkblue', scatter_kws={'s': 15})
      plt.xlabel('Temperature')
      plt.ylabel('Count')
      plt.title('Korelasi Temperature dengan Total Banyaknya Peminjam Sepeda', fontsize = 20,fontweight='bold')
      st.pyplot(plt)
    if __name__ == '__main__':
        main()

col1, col2 = st.columns(2)
with col1:
    def main():
      st.subheader('Hubungan antara Apparent Temperature dengan Total Banyaknya Peminjam Sepeda')
      st.write('Hubungan antara apparent temperatur dan total peminjam sepeda merupakan hubungan yang positif, artinya bahwa ketika temperatur rendah maka total peminjam sepeda juga rendah dan berlaku sebaliknya. Grafik yang terbentuk memiliki kemiringan yang signifikan dan titik-titiknya menyebar mendekati garis tersebut maka dapat dikatakan bahwa apparent temperatur secara signifikan mempengaruhi total peminjaman sepeda.')
      sns.set(style="whitegrid")
      plt.figure(figsize=(10, 6))
      sns.regplot(x=day_df['atemp'], y=day_df['cnt'], color='darkblue', scatter_kws={'s': 15})
      plt.xlabel('Apparent Temperature')
      plt.ylabel('Count')
      plt.title('Korelasi Apparent Temperature dengan Total Banyaknya Peminjam Sepeda', fontsize = 20,fontweight='bold')
      st.pyplot(plt)
    if __name__ == '__main__':
       main()

 
with col2:
    def main():
      st.subheader('Hubungan antara Windspeed dengan Total Banyaknya Peminjam Sepeda')
      st.write('Hubungan antara windspeed dan total peminjam sepeda merupakan hubungan yang negatif, artinya bahwa ketika windspeed rendah maka total peminjam sepeda tinggi/meingkat. Namun karena grafik yang terbentuk kemiringannya tidak terlalu signifikan dan titik-titiknya terlihat masih menyebar, maka dapat dikatakan bahwa windspeed kurang secara signifikan mempengaruhi total peminjaman sepeda.')
      sns.set(style="whitegrid")
      plt.figure(figsize=(10, 6))
      sns.regplot(x=day_df['windspeed'], y=day_df['cnt'], color='darkblue', scatter_kws={'s': 15})
      plt.xlabel('Windspeed')
      plt.ylabel('Count')
      plt.title('Korelasi Windspeed dengan Total Banyaknya Peminjam Sepeda', fontsize = 20,fontweight='bold')
      st.pyplot(plt)
    if __name__ == '__main__':
        main()
