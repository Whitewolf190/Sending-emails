import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()


try:

    newid = input("Enter Senders Email id : ")
    password = input("Enter senders password : ")
        
    s.login(newid,password)
        
    receiver_id = input("Enter receivers Email id : ")
    Subject = input("Enter Subject of your Email : ")
    Body = input("Enter body of your Email : ")
    message = 'Subject: {}\n\n{}'.format(Subject, Body)
        

    s.sendmail(newid,receiver_id,message)

    print("Message sent")
    s.quit()
except smtplib.SMTPAuthenticationError:    
    print("""Your Email is not sent""")
    

except:    
    print("Email not sent")