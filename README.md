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
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/5bd0e1cc-2680-4bba-87bf-b00f27c1d8e4)

![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/b605a3e7-7427-4b18-93b8-e7e3989d4080)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/11a92b9b-4143-4ea9-a488-ba60584b6813)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/09db418e-65cd-4cbc-880f-4c9027dde182)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/6a7cab34-1999-45eb-a464-c3f8bd7a66e5)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/6a7cab34-1999-45eb-a464-c3f8bd7a66e5)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/70c85f48-046f-4e65-9f04-5511523abb9c)
![image](https://github.com/pangestikamp/proyekakhir1/assets/162313682/22583525-7f6b-4419-953e-a771435398bf)





