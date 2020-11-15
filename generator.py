##Generate captcha imgs

from captcha.image import ImageCaptcha
import sqlite3
from random import randint

image = ImageCaptcha()

sql = sqlite3.connect('db.sqlite3')
# sql.execute("CREATE TABLE Imgs (ID SERIAL PRIMARY KEY , PATH VARCHAR NOT NULL , CODE VARCHAR NOT NULL);")
# sql.commit()

for x in range(1, 30):
    number = randint(1111, 9999)
    path = 'imgs/%s.png'%x
    sql.execute("INSERT INTO IMGS (ID, PATH, CODE) VALUES(?,?,?)", (x, path, number))
    sql.commit()
    image.write(str(number), path)
