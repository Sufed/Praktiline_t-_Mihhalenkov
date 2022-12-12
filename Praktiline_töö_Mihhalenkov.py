#12/12/22
from math import *
from random import *
try:
    päev=int(input("Mis päev täna on? "))
    if päev==7:
        print("Täna on pühapäev.")
    elif päev==6:
        print("Täna on laupäev.")
    elif päev==5:
        print("Täna on reede.")
    elif päev==4:
        print("Täna on neljapäev.")
    elif päev==3:
        print("Täna on kolmapäev.")
    elif päev==2:
        print("Täna on teisipäev.")
    elif päev==1:
        print("Täna on esmaspäev.")
except:
    print("MIS PÄEV TÄNA ON???")
print()
print()
print()
from math import *
from random import *
#12/12/22
try:
    hinne=int(input("Mis hinne täna sai koolis? "))
except:
    print("KURAT!!!")
if hinne==5:
    print("Väga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Hea")
elif hinne==2 or hinne==1: #and, or, not (!=) ei võrdu, <, >, >=, <=
    print("Miite rahuldav!")
else:
    print("Viga!")
#Kümnes harjutus #Преобразование времени Пользователь вводит время в минутах Ваша формула находит и выводит часы и минуты Например: введите 72, ответ 1:12
from math import *
from random import *
print("Kümne harjutus")
try:
    a=float(input("Aega minutit: "))
except:
    print("Vale andmetüüp!")    
#ti=(a/60)%60
try:
    ti=int(a//60)
except:
    print("Vale andmetüüp!")
try:
    ti1=int(a%60)
except:
    print("Vale andmetüüp!")

print(f"{ti}:{ti1}")
print()
print()
print()
#Üheksas harjutus
from math import *
from random import *
print("Üheksas harjutus") #Средняя скорость ролика 29,9км/ч Как далеко можно добраться за 24 минуты
b=24/60 #b=randint(1,60)
a=b*29.9 #a=randint(1,100)
print(f"{a} km {b} h")
#print(f"Nii palju {t} km saab sõita {b} min")
print()
print()
#Kaheksas harjutus
from math import *
from random import *
print("Kaheksas harjutus")
a=randint(1,100) #Сколько залил литров
b=randint(1,100) #Пройденный километры
print(f"a={a}\n b={b}\n")
T=(a/b)*100
print(f"Kütusekulu: {round(T,2)}")
print()
print()
print()
#Seitse harjutus #Вы взяли большую пиццу с 3 друзьями за 12,90 евро. Вы оставили официанту 10% чаевых. Создайте программу, которая определяет, сколько каждый должен заплатить.
print("Seise harjutus")
from math import *
P=12.90 #цена пиццы
n=0.10 #чаевые
S=(P+n)/3
print(f"Nii palju jootraha peab andma 1 inimene. {round(S,2)}")
print()
print()
print()
#Kuue harjutus
from math import * 
from random import *
print("Kuue harjutus")
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
# print(f"Kolmnurga ümbermõõt = {a+b+с}")
P=a+b+c
print(f"P: {round(P,2)}" + " m**2")
print()
print()
#Viie harjutus
print("   @..@")
print("  (----)")
print("  ( \__/ )")
print("  ^^ '' ^^  ")
print()
print()
print()
#Neljandal harjutus
from math import * 
print("Neljandal harjutus")
try:
    q=int(input("q pikkus: "))
except:
    print("Vale andmetüüp!")
try:
    w=int(input("w pikkus: "))
except:
    print("Vale andmetüüp!")
try:
    e=int(input("e pikkus: "))
except:
    print("Vale andmetüüp!")
try:
    r=int(input("r pikkus: "))
except:
    print("Vale andmetüüp!")
try:
    t=int(input("t pikkus: "))
except:
    print("Vale andmetüüp!")
Sr=(q+w+e+r+t)/5
print()
print(f"Keskmine on {Sr}")
print()
print()
print()
#Kolmandal harjutus
print("Kolmandal harjutus")
try:
    aeg=float(input("Mitu tundi kulus sõiduks? "))
except:
    print("Vale andmetüüp!")
try:
    teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
except:
    print("Vale andmetüüp!")
kiirus=aeg/teepikkus
print()
print("Sinu kiirus oli " + str(round(kiirus,2)) + " km/h")
print()
#Teine harjutus
from math import * 
print("Teine harjutus")
try:
    a=float(input("pikkus N: "))
except:
    print("Vale andmetüüp!")
try:
    b=float(input("pikkus M: "))
except:
    print("Vale andmetüüp!")
d=sqrt(a**2+b**2)
print()
print(f"Maatuki diagonaal on {round(d,2)} m**2")
print()
print()
print()
#Esimene harjutus
from math import * 
print("Esimene harjutus")
try:
    C=float(input("Ümbermõõt: "))
except:
    print("Vale andmetüüp!")
r=C/(2*pi)
di=2*r
print()
print("Ümbermõõt võrdub:", round(di,2))
print("Puu läbimõõduga:", (C))

#print(f"Vastus:\nPuu {C}") #\n нажимает Enter