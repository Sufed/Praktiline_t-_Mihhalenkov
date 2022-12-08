#Kümne harjutus #Преобразование времени Пользователь вводит время в минутах Ваша формула находит и выводит часы и минуты Например: введите 72, ответ 1:12
from math import *
from random import *
print("Kümne harjutus")
a=float(input("Aega minutit: "))
#ti=(a/60)%60
ti=(a//60%60)
ti1=(a%60)

print(ti,ti1)
print()
print()
print()
#Üheksas harjutus
from math import *
from random import *
print("Üheksas harjutus") #Средняя скорость ролика 29,9км/ч Как далеко можно добраться за 24 минуты
a=29.9 #a=randint(1,100)
b=24 #b=randint(1,60)
Pu=a/b
print(f"Nii palju {round (Pu,2) } km saab sõita {b} min")
print()
print()
print()
#Kaheksas harjutus
from math import *
from random import *
print("Kaheksas harjutus")
a=randint(1,100) #Сколько залил литров
b=randint(1,100) #Пройденный километры
с=randint(1,50) #Оставшееся топливо
print(f"Külg a={a}\nKülg b={b}\nKülg c={с}")
T=(с/b)*100
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
q=int(input("q pikkus: "))
w=int(input("w pikkus: "))
e=int(input("e pikkus: "))
r=int(input("r pikkus: "))
t=int(input("t pikkus: "))
Sr=(q+w+e+r+t)/5
print()
print(f"Keskmine on {Sr}")
print()
print()
print()
#Kolmandal harjutus
print("Kolmandal harjutus")
aeg=float(input("Mitu tundi kulus sõiduks? "))
teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
kiirus=aeg/teepikkus
print()
print("Sinu kiirus oli " + str(round(kiirus,2)) + " km/h")
print()
#Teine harjutus
from math import * 
print("Teine harjutus")
a=float(input("pikkus N: "))
b=float(input("pikkus M: "))
d=sqrt(a**2+b**2)
print()
print(f"Maatuki diagonaal on {round(d,2)} m**2")
print()
print()
print()
#Esimene harjutus
from math import * 
print("Esimene harjutus")
C=float(input("Ümbermõõt: "))
r=C/(2*pi)
di=2*r
print()
print("Ümbermõõt võrdub:", round(di,2))
print("Puu läbimõõduga:", (C))

#print(f"Vastus:\nPuu {C}") #\n нажимает Enter