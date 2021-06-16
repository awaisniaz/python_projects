import smtplib
sender_mail = 'owais.niaz@targetofs.com'
receivers_mail  = ['awaisniaz1995@gmail.com']
message = "Hello mer jan"


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender_mail,receivers_mail,message)
    print("Your reciver receive your mail")
except Exception as e:
    print("Sorry try Again")
    print(e)