sayi1 = 10
sayi2 = 200
sayi3 = 50

#print("En Büyük Sayı : "+ str(sayi3))
#sayi3 integer olduğu için string ile tamsayıyı toplayamaz, str tamsayıyı string tipine çevir demek.

if sayi1>sayi2 and sayi1>sayi3:
    print("En Büyük Sayı : "+ str(sayi1))
elif sayi2>sayi1 and sayi2>sayi3:
    print("En Büyük Sayı : "+ str(sayi2))
else:
    print("En Büyük Sayı : "+ str(sayi3))
