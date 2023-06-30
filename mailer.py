import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_mail():
    
        message = MIMEMultipart()
        message["To"] = 'Mansuri Hussain'
        message["From"] = 'Hussain Mansuri'
        message["Subject"] = 'TEST MAIL'

        title = '<b> TESTING EMAIL SENDING PYTHON CODE </b>'
        messageText = MIMEText('''This mail was sent from my python code.''','html')
        message.attach(messageText)

        email = 'mansurihussain12345@gmail.com'
        password = 'lnqpdrsvuqeuuzze'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo('Gmail')
        server.starttls()
        server.login(email,password)
        fromaddr = 'mansurihussain12345@gmail.com'
        toaddrs  = 'hussainmansuri12345@gmail.com'
        server.sendmail(fromaddr,toaddrs,message.as_string())

        server.quit()


send_mail()
