from flask import Flask, render_template, request, redirect, flash
from app.modules.module import db_instert, mail_sender, mail_config, form_getter, querysearch
import time
import datetime

app = Flask(__name__)

# email connection
reciever, mail = mail_config(app)
app.secret_key = "asdfhhdkfsahkdfas"


@app.route("/", methods=['post', 'get'])
def ThePage():
    if request.method == "POST":

        try:
            ad, soyad, email, sinif, refkod, message = form_getter(request)
        except:
            flash(
                "Bir hata meydana geldi, lütfen daha sonra tekrar deneyiniz. Hatanın tekrarı durumunda bize iletişim adreslerimizden ulaşabilirsiniz.")
            return redirect("/#formdoldur")

        db_task = db_instert(ad=ad,
                             soyad=soyad,
                             email=email,
                             sinif=sinif,
                             refkod=refkod,
                             message=message,
                             time=str(datetime.date.today()))
        if db_task:
            doc = querysearch()
            last_submitted = []
            for i in doc:
                last_submitted.append({"ad": i["ad"], "soyad": i["soyad"]})
            print("Succesfully saved")
        else:
            print("an error happened")

        mail_task = mail_sender(mail,
                                ad,
                                soyad,
                                sinif,
                                email,
                                refkod,
                                message,
                                reciever,
                                reciever)
        if mail_task:
            print("Succesfully send")
        else:
            print("an error hapened")

        if db_task and mail_task:
            time.sleep(0.4)
            flash("İlginiz için çok teşekkür ederiz mesajınızı aldık, bir gün içinde size döneceğiz.")
            return render_template("index.html", last_list=last_submitted)
        else:
            return redirect("/")
    else:
        return render_template("index.html")
