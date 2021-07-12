import pymongo
from flask_mail import Mail, Message


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["YksKocumDB"]
mycol = mydb["Submits"]

#saving data to database
def db_instert(**kwargs):
    data_instance = {}
    for key, value in kwargs.items():
        data_instance[key] = value
    try:
        status = mycol.insert_one(data_instance)
        if status.acknowledged:
            return True
    except:
        return False

def querysearch():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["YksKocumDB"]
    mycol = mydb["Submits"]
    doc = mycol.find().sort("time").limit(5)
    return doc


#maintaining mail connection
def mail_config(app):
    reciever = "kahvesahane@outlook.com"
    app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = reciever
    app.config['MAIL_PASSWORD'] = '2220197ks'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail = Mail(app)
    return reciever,mail

#sending mail
def mail_sender(mail, ad, soyad, sinif, email, refkod, message, sender, reciever):
    subject = """Öğrenci adı soyadı: """ + ad + " " + soyad + " sınıfı: " + str(sinif)
    body = """Bu web'den gelen bir maildir.\n""" + "Öğrenci maili: " + email + "\nrefcode: " + refkod + " \n\nmessage: " + message
    try:
        msg = Message(subject=subject,
                      body=body,
                      sender=reciever,
                      recipients=[reciever])
        mail.send(msg)
        return True
    except:
        return False

#data flow from form in html
def form_getter(request):
    ad = request.form.get("ad")
    soyad = request.form.get("soyad")
    email = request.form.get("email")
    sinif = request.form.get("sinif")
    refkod = request.form.get("refkod")
    message = request.form.get("message")
    return ad,soyad,email,sinif,refkod,message




