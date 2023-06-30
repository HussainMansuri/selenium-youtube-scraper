import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def gmail_send_mail(to_name,from_name,subject,message_body,login_email,login_password,from_addrs,to_address):
    
        message = MIMEMultipart()
        message["To"] = to_name
        message["From"] = from_name
        message["Subject"] = subject

        # title = '<b> TESTING EMAIL SENDING PYTHON CODE </b>'
        messageText = MIMEText(message_body,'html')
        message.attach(messageText)

        email = login_email
        password = login_password

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo('Gmail')
        server.starttls()
        server.login(email,password)
        fromaddr = from_addrs
        toaddrs  = to_address
        server.sendmail(fromaddr,toaddrs,message.as_string())

        server.quit()



