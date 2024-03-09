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


## Library yang dibutuhkan
```
pip install pandas
pip install matplotlib
pip install numpy
pip install seaborn
pip install streamlit
```
## Run streamlit app
```
streamlit run dashboard.py
```
### Tampilan Dashboard
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/ac9e4024-28d3-4753-9929-08791cd6880c)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/6d7b2595-41c4-4c96-86cf-8c311e257f93)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/8486bf8a-c756-4da2-83ea-1040430b9016)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/ddedcf36-3904-426d-83c2-727989462d06)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/96dc232f-a600-4096-b356-a172176287ed)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/7333bbec-175d-4909-816b-30b059961199)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/ebe35cd4-d519-4cb6-a6c9-6474f1bf38b6)




