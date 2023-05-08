import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_buku"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE toko_buku")
'''mycursor.execute("SHOW DATABASEs")
for x in mycursor:
    print(x)'''
#mycursor.execute("CREATE USER 'dhea'@'localhost' IDENTIFIED BY 'dhea'")
#mycursor.execute("CREATE TABLE pelanggan (nama VARCHAR(255),id_pelanggan INT(11),alamat VARCHAR(255),noHp VARCHAR(15))")
#mycursor.execute("GRANT SELECT (alamat,noHp),INSERT (noHp) ON toko_buku.pelanggan TO 'dhea'@'%';")
#mycursor.execute("GRANT SELECT (alamat,noHp),INSERT (noHp) ON toko_buku.pelanggan TO 'dhea'@'%' REQUIRE SSL;")
mycursor.execute("GRANT SELECT (alamat,noHp),INSERT (noHp) ON toko_buku.pelanggan TO 'dhea'@'%' REQUIRE X509;")
#mycursor.execute("GRANT SELECT (alamat,noHp),INSERT (noHp) ON toko_buku.pelanggan TO 'dhea'@'%' REQUIRE CIPHER 'RSA-EDH-CBC3-DES-SHA';")
#mycursor.execute("GRANT SELECT (alamat,noHp),INSERT (noHp) ON toko_buku.pelanggan TO 'dhea'@'%' REQUIRE ISSUER 'C=ZA, ST=Western Cape,L=CapeTown, O=Thawte Consulting cc, OU=Certification ServicesDivision,CN=Thawte Server CA/emailAddress=servercerts@thawte.com’;")
#mycursor.execute("GRANT SELECT (alamat,noHp),INSERT (noHp) ON toko_buku.pelanggan TO 'dhea'@'%' REQUIRE SUBJECT 'C=US, ST=California,L=Pasadena, O=Indiana Grones, OU=Raiders,CN=www.lostarks.com/emailAddress=indy@lostarks.com';")
