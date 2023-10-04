# HESAP MAKİNESİ

from tkinter import *

# Sayıları giriş kutusuna ekleyen fonksiyon
def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))

# Hesaplama için kullanılacak global değişkenler
hesap = 5
sayi1 = 0
sayi2 = 0

# İşlem türünü belirleyen fonksiyon
def islemler(x):
    global hesap
    hesap = x
    global sayi1
    sayi1 = float(giris.get())
    giris.delete(0, 'end')

# Hesaplama işlemini gerçekleştiren fonksiyon
def hesapla():
    global sayi2
    sayi2 = float(giris.get())
    global hesap
    sonuc = 0
    if (hesap == 0):
        sonuc = sayi1+sayi2
    elif (hesap == 1):
        sonuc = sayi1-sayi2
    elif (hesap == 2):
        sonuc = sayi1*sayi2
    elif (hesap == 3):
        sonuc = sayi1/sayi2
    giris.delete(0, 'end')
    giris.insert(0, str(sonuc))

# Tkinter penceresini oluşturma
pencere = Tk()
pencere.title("Hesap Makinesi")

# pencere boyutlarını ayarlama
pencere.geometry("350x400")

# veri giriş kutusu oluşturma
giris = Entry(font="Verdana 15 bold", width=15, justify="right")
giris.place(x=20, y=20)


# rakam butonları oluşturma ve özelliklerini ayarlama
b = []
for i in range(1, 10):
    b.append(Button(text=str(i), font="Verdana 14 bold",
             command=lambda x=i: yaz(x)))


# rakam butonlarının yerleşimi
sayac = 0

for i in range(0, 3):
    for j in range(0, 3):
        b[sayac].place(x=20+j*60, y=60+i*60)
        sayac += 1


# işlem butonları oluşturma ve özelliklerini ayarlama
islem = []

for i in range(0, 4):
    islem.append(Button(font="Verdana 14 bold",
                 width=2, command=lambda x=i: islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "x"
islem[3]['text'] = "/"

# işlem butonlarının yerleşimi
for i in range(0, 4):
    islem[i].place(x=190, y=60+i*60)

sifirbutonu = Button(text="0", font="Verdana 14 bold",
                     command=lambda x=0: yaz(x))
sifirbutonu.place(x=20, y=240)

noktabutonu = Button(text=".", font="Verdana 14 bold",
                     width=2, command=lambda x=".": yaz(x))
noktabutonu.place(x=80, y=240)

esittirbutonu = Button(text="=", font="Verdana 14 bold", command=hesapla)
esittirbutonu.place(x=140, y=240)

temizlemebutonu = Button(text="Temizle", fg="red",
                         font="Verdana 14 bold", command=lambda: giris.delete(0, 'end'))
temizlemebutonu.place(x=20, y=300)

Silmebutonu = Button(text="Sil", fg="orange", font="Verdana 14 bold",
                     command=lambda: giris.delete(len(giris.get()) - 1, 'end'))
Silmebutonu.place(x=140, y=300)

pencere.mainloop()
