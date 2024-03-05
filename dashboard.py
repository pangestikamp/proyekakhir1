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
st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Musim')
st.write('Total peminjam sepeda pada tahun 2011 mengalami peningkatan yang signifikan di tahun 2012 pada setiap musim. Urutan dari tertinggi ke terendah total peminjam sepeda berdasarkan musim yaitu musim gugur, musim dingin, musim panas, dan terakhir musim semi. Urutan tersebut berlaku untuk tahun 2011 dan 2012.')
fig, ax = plt.subplots()
sns.barplot(data=day_df, x='season', y='cnt', hue='yr', ax=ax, ci=None)
plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Jumlah Peminjaman Sepeda Berdasarkan Musim')
plt.legend(title='Year')
st.pyplot(fig)

st.subheader('Pola Peminjaman Sepeda')
st.write('Tahun 2011 dan 2012 memiliki pola yang sama, yaitu sama-sama membentuk kurva cembung. Meskipun terjadi peningkatan pada tahun 2012 namun pola grafiknya terlihat sama. Hal tersebut terjadi karena pembentukan kurva dipengaruhi oleh musim yang terjadi, dimana musim-musim tersebut akan berulang pada setiap tahunnya.')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df["dteday"],
    day_df["cnt"], 
    linewidth=1,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)