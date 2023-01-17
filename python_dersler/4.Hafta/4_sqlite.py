import sqlite3

bag = sqlite3.connect("a.vt")
# Tabloya bağlan.

cursor = bag.cursor()
# cursor isimli değişken veri tabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)") # Sorguyu çalıştırıyoruz.
bag.commit() # Sorgunun veri tabanı üzerinde geçerli olması için commit işlemi gerekli.


bag.close() # Bağlantıyı koparır.