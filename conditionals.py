istenenKredi = 100000
hesap = 9600
minimumOlmasiGerekenHesap = 10000

if hesap>=minimumOlmasiGerekenHesap:
    print("Kredi Verilebilir.")
    print("ödemeler hesaplandı.")
elif hesap>=9000 and hesap<=9500:
    print("Müdüre sorulacaktır.")
elif hesap>=9501 and hesap<=9999:
    print("Genel müdüre sorulacaktır.")
else:
    print("Kredi almak için bakiyeniz yetersizdir.")
print("işlem sonu.")
