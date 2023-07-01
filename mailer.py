'''
This was used to check mailing functionality and is no longer reqired to be imported in code as it has been written in the main "scraper.py" file
'''

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders



# def gmail_send_mail(to_name,from_name,subject,message_body,login_email,login_password,from_addrs,to_address,file_name=None):
    
#         message = MIMEMultipart()
#         message["To"] = to_name
#         message["From"] = from_name
#         message["Subject"] = subject

#         # title = '<b> TESTING EMAIL SENDING PYTHON CODE </b>'
#         messageText = MIMEText(message_body,'html')
#         message.attach(messageText)
        
#         if file_name:
#                 try:
#                         print('File found to attach')
#                         attachment= open(file_name,'rb')
        

#                         #Encode file in base64
#                         attachment_package = MIMEBase('application', 'octet-stream')
#                         attachment_package.set_payload((attachment).read())
#                         encoders.encode_base64(attachment_package)
#                         attachment_package.add_header('Content-Disposition', "attachment; filename= " + file_name)
#                         message.attach(attachment_package)
#                 except:
#                         print(f"Failed to attach file: {file_name}")
#                 else:
#                         print("File attached successfully!")


#         email = login_email
#         password = login_password
#         try:
#                 mail_server = 'smtp.gmail.com:587'
#                 dns_name = 'GMAIL'
#                 server = smtplib.SMTP(mail_server)
#                 server.ehlo(dns_name)
#                 server.starttls()
#                 server.login(email,password)
#                 fromaddr = from_addrs
#                 toaddrs  = to_address
#                 server.sendmail(fromaddr,toaddrs,message.as_string())
#         except:
#                 print(f"Failed to connect to the mail server: {mail_server} with DNS: {dns_name} !!")
#         else:
#                 print("Email sent!, shutting down server connection.")
#                 server.quit()



