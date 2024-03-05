# Proyek Akhir 1 ✨

## Bike Sharing Dataset
Berisi data jumlah peminjam sepeda setiap hari dari tahun 2011 - 2012. Berikut beberapa variabelnya:
1. instant: record index
2. dteday : date
3. season : season (1:springer, 2:summer, 3:fall, 4:winter)
4. yr : year (0: 2011, 1:2012)
5. mnth : month ( 1 to 12)
6. hr : hour (0 to 23)
7. holiday : weather day is holiday or not (extracted from [Web Link])
8. weekday : day of the week
9. workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
10. temp : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
11. atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
12. hum: Normalized humidity. The values are divided to 100 (max)
13. windspeed: Normalized wind speed. The values are divided to 67 (max)
14. casual: count of casual users
15. registered: count of registered users
16. cnt: count of total rental bikes including both casual and registered
```
### Library yang dibutuhkan
1. Pandas
2. Matplotlib
3. Numpy
4. Seaborn
5. Streamlit
## Run streamlit app
```
streamlit run dashboard.py
```
### Tampilan Dashboard
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/ad423bb6-1732-4a4a-8761-262ac69cd738)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/e782bc6e-8299-48e7-afd5-c666ac31ce48)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/db5bb2d4-bf41-44dd-8262-36b71b94055c)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/5099fa5d-ef44-4e53-b66d-1472f1e06dc5)




