def dene():
    print("Deneme working")

# Eğer burada bu ifadeyi koymazsak, bu modül import edildiğinde dene() fonksiyonu otomatik çalışır.
# Diyeceksin e neden fonksuyonun caller ını comment yapmıyoruz. Nedeni python3 dene() diye shell den
# modül çalıştırılmak istenirse çalışmalı. Bu yüzden name == main ise çalış diyoruz.
# Kısaca modülümüz hem import edilebilmeli, hem de python shell den çalıştırılabilmeli.
if __name__ == '__main__':
    dene()