urunler = ["Laptop" , "Mouse" , "Keyboard"]
print(urunler)
print(type(urunler))

urunler.append("Telefon")
print(urunler)

ogrenciler1 = ["Salih" , "Ayşe" , "Ahmet"]
ogrenciler2 = ["Ali" , "Zehra" , "Musa"]

ogrenciler1 = ogrenciler2
ogrenciler2[0] = "Engin"
print(ogrenciler1)
print(ogrenciler2)
#burada değer ve referans tip dediğimiz durum söz konusudur.

sayi1 = 10
sayi2 = 48
sayi1 = sayi2
sayi2 = 60
print(sayi1)

#referans tip -> list
#değer tip -> int        sayısal veri tipleri değer tiptir.
#string, referans tiptir. ama birçok programlama dilinde değer tip gibi sonuç döndürür.

isim = "Mukaddes"  #aslında burada karakterlerden oluşan bir liste var.
print(isim[0])

#if'in az kullanımı programın kalitesini gösterir.
#bir projede ki if sayısı o projenin ne kadar nesnel yazıldığıyla ters orantılıdır.

bosListe = []

#devops = yazılım geliştirme süreç yönetimi için kullanılan kısa isimlendirmedir. developer operations
# dsadw