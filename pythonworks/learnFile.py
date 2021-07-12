import asyncio
import math
import threading


# asyncio
async def islem(n):
    l = range(n)
    for i in l:
        print(i)
        await asyncio.sleep(0.1)

async def curser(name, r):
    for i in range(r):
        print(name, "sen orrospuı çucyğusun")
        await asyncio.sleep(0.05)

async def fun(*args,**kwargs):
    await asyncio.sleep(1)
    for i in args:
        print(math.factorial(i))
        await asyncio.sleep(0.04)
    for name, surname in kwargs.items():
        print(f"here is a data named {name}, surnamed {surname}")
        await asyncio.sleep(0.04)



async def iotask():
    task = asyncio.create_task(islem(10))
    task2 = asyncio.create_task(curser("ata", 10))
    task3 = asyncio.create_task(fun(*(range(20)), **{"hakan":"akgün", "berkay":"yalçınkaya"}))
    print("SAA")
    await task3

#metaclass
class meta(type):
    def __new__(self, class_name, bases, attrs):
        a = {"school":"FSFL", "age":18}
        for name, value in attrs.items():
            a[name] = value
        return type(class_name, bases , a)

class ogrenci(metaclass= meta):
    Sınıf = "12/B"

kaan = ogrenci()

print(kaan.school, kaan.age, kaan.Sınıf)

import time
ls=[]
def fun2(*args):
    for i in args:
        print(i)
        time.sleep(1)
        ls.append(i)
    print("finished")

#x = threading.Thread(target=fun2, args=(range(5)))
#x.start()

#y = threading.Thread(target=fun2, args=(range(100,111)))
#y.start()

#print(ls)
#y.join()
#print(ls)


#generator

def gen(n):
    for i in range(n):
        yield i**i*i*i

#for i in gen(10):
#   print(i)

#mail

#reciever = "kahvesahane@outlook.com"

#app.config['MAIL_SERVER']='smtp-mail.outlook.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USERNAME'] = reciever
#app.config['MAIL_PASSWORD'] = '2220197ks'
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = False
#mail = Mail(app)



#subject = """Öğrenci adı soyadı: """ +ad+ " " +soyad+ " sınıfı: " +str(sinif)
        #       body = """Bu web'den gelen bir maildir.\n""" +"Öğrenci maili: "+ email +"\nrefcode: " + refkod +" \n\nmessage: " + message
        #print("cycle starts")

        #try:
        #   msg = Message(subject=subject,
        #                 body=body,
        #                 sender=reciever,
        #                 recipients=[reciever])
        #   mail.send(msg)
        #   return redirect("/#formdoldur")
        #except:
        #   print("cycle ends")
#


import math

#int(input("yarıçap: "))
#int(input("yükseklik: "))

#alan= (math.pi * int(input("yükseklik: ")) * int(input("yarıçap: "))**2)/3
#çevre = (2* (((int(input("yarıçap: "))**2)+(int(input("yükseklik: "))**2))**1/2) + 4*int(input("yarıçap: ")) * math.pi)

print("Alan: " , (math.pi * int(input("yükseklik: ")) * int(input("yarıçap: "))**2)/3 ,"\n" , "Çevre: " , (2* (((int(input("yarıçap: "))**2)+(int(input("yükseklik: "))**2))**1/2) + 4*int(input("yarıçap: ")) * math.pi))

