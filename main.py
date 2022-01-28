import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

print("Program pengirim email otomatis")
print("Isi data berikut")

#setup alamt email pengirim dan penerima
email_send = "baraannanda20@gmail.com"
pw_send = "sandibaru2002"
email_receiver = "barawima123@gmail.com"
print(" ")

#setup MIME
message = MIMEMultipart()
message['From'] = email_send
message['To'] = email_receiver
message['Subject'] = input(str("isi subjek email : "))

#setup body email
#example file body email : "body_email.txt"
x = 1
while x == 1:
    print("Pilihan body email : ")
    print("1. Input manual")
    print("2. Input file")
    pilihan = int(input("Pilihan : "))
    if pilihan == 1:
        body_email = input(str("Body Email: "))
        message.attach(MIMEText(body_email,'plain'))
        x = 0
    elif pilihan == 2:
        nama_file = input(str("Nama file (Dengan jenis folder, Ex : 'body_email.txt') : "))
        message.attach(MIMEText(open(nama_file).read()))
        x = 0
    else :
        print("Tidak ada dalam pilihan, mohon masukkan dengan benar !!!")
        x = 1

#setup attachment
#3 example attatchment : gambar_email.jpg , data_email.xlsx , laporan_email.docx
tot_att = []
total = int(input("Total attachment : "))
z = 0
if total <= 0 :
  pass
else :
    for i in range(total) :
        tot_att.append(z)
        print("[{}] Masukkan nama file (Dengan jenis folder, Ex : 'isi_email.txt' ) : ".format(z+1))
        nama = input(str("Nama file : "))
        tot_att[z] = MIMEApplication(open(nama,'rb').read())
        tot_att[z].add_header('Content-Disposition', 'attachment', filename= nama)
        message.attach(tot_att[z])
        z = z + 1

#Setup SMTP Sessions
try:
    session = smtplib.SMTP_SSL('smtp.gmail.com',465)
    session.ehlo()
    session.login(email_send, pw_send)
    text = message.as_string()
    session.sendmail(email_send,email_receiver, text)
    session.quit()
    print("Email telah terikirim")
except Exception as exception:
    print("Error: %s!\n\n" % exception)